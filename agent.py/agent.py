"""
SyllabusPilot — Agent Module
Standalone Gemini-powered extraction and planning logic.
Can be imported by app.py or run independently.
"""

import os
import json
import re
from dotenv import load_dotenv
from google import genai

# Load .env from the nested path our project uses
_env_path = os.path.join(os.path.dirname(__file__), "..", ".env", ".env")
load_dotenv(dotenv_path=_env_path)

MODEL = "gemini-flash-latest"


def get_client() -> genai.Client:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("GEMINI_API_KEY not set. Check your .env file.")
    return genai.Client(api_key=api_key)


def _strip_json(text: str):
    """Remove markdown fences and parse JSON."""
    text = re.sub(r"```(?:json)?", "", text).strip().strip("`").strip()
    return json.loads(text)


def extract_tasks(syllabus_text: str) -> list[dict]:
    """
    Send syllabus text to Gemini and return a list of extracted task dicts.
    Each dict has: course, task, type, deadline, weight, status, notes
    """
    client = get_client()
    prompt = f"""
You are SyllabusPilot, an expert academic planning assistant.

Extract every assignment, exam, quiz, project, lab, midterm, final, and milestone from this syllabus.

Return ONLY a valid JSON array — no markdown, no commentary.

Each element:
{{
  "course": "Course name or 'Unknown Course'",
  "task": "Task name",
  "type": "Assignment | Exam | Quiz | Project | Lab | Milestone | Other",
  "deadline": "YYYY-MM-DD or Unknown",
  "weight": "e.g. '20%' or Unknown",
  "status": "Upcoming",
  "notes": "Any conflicts/ambiguities, or empty string"
}}

Rules:
- Never invent dates or percentages.
- Mark unclear values as Unknown.
- Note conflicts in the notes field.

SYLLABUS:
{syllabus_text}
"""
    response = client.models.generate_content(model=MODEL, contents=prompt)
    return _strip_json(response.text)


def generate_study_plan(
    tasks: list[dict],
    hours_per_week: float,
    preferred_days: list[str],
    unavailable_days: list[str],
    today_str: str | None = None,
) -> list[dict]:
    """
    Generate a week-by-week study plan given tasks and student preferences.
    Returns a list of week dicts with 'week', 'tasks', 'total_hours'.
    """
    from datetime import date

    client = get_client()
    today = today_str or date.today().isoformat()
    days_str = ", ".join(preferred_days) if preferred_days else "Any day"
    unavail_str = ", ".join(unavailable_days) if unavailable_days else "None"

    prompt = f"""
You are SyllabusPilot's study planner.

Student preferences:
- Weekly study hours: {hours_per_week}
- Preferred study days: {days_str}
- Unavailable days: {unavail_str}
- Today's date: {today}

Tasks to plan (JSON):
{json.dumps(tasks, indent=2)}

Return ONLY a valid JSON array — no markdown, no commentary.

Each element:
{{
  "week": "Week N (Month Day – Month Day)",
  "tasks": [
    {{
      "course": "Course name",
      "task": "What to study",
      "hours": 2.5,
      "notes": "e.g. Review lecture notes before midterm"
    }}
  ],
  "total_hours": 9.0
}}

Rules:
- Total hours per week ≤ {hours_per_week}.
- Prioritise earlier deadlines.
- Balance workload across courses.
- Add review sessions before exams.
- Do not schedule on unavailable days (note it instead).
"""
    response = client.models.generate_content(model=MODEL, contents=prompt)
    return _strip_json(response.text)


# Quick smoke-test when run directly
if __name__ == "__main__":
    sample = """
    CS101 Introduction to Computer Science
    Professor: Dr. Smith

    Assignments:
    - Assignment 1: Variables and Data Types — Due: 2025-02-14 — Weight: 10%
    - Assignment 2: Control Flow — Due: 2025-03-07 — Weight: 10%
    - Midterm Exam — Due: 2025-03-15 — Weight: 30%
    - Final Project — Due: 2025-04-30 — Weight: 30%
    - Final Exam — Due: 2025-05-10 — Weight: 20%
    """
    print("Extracting tasks…")
    tasks = extract_tasks(sample)
    print(json.dumps(tasks, indent=2))
