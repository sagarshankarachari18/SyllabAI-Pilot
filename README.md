# 🎓 SyllabusPilot — AI University Study Planner

**SyllabusPilot** is an executive academic command center built for university students. Upload course syllabus files (PDF, text) or load sample courses, let Google Gemini extract deadlines and assessment weights, and generate an optimized weekly study plan with real-time rescheduling, language selection, notifications, and calendar sync.

---

## ✨ Features

- 👤 **Executive Professional Dashboard**:
  - **Personalized Greeting**: Displays the student's name (e.g. *Welcome back, Alex Morgan 👋*) with editable profile.
  - **Current Semester & Academic Progress**: Tracks term progress (*Fall 2026 · Week 9 of 16 · Midterms Period*) with an interactive progress bar showing deliverables completed.
  - **Courses Uploaded Overview**: Active course cards and course code tags.
  - **Upcoming Assignments & Exams Cockpit**: Prioritizes imminent deadlines with color-coded urgency badges (*"Due in 2 days"*, *"Due Today!"*), exam warnings, weight impacts, and 1-click status completion.
  - **Study Hours Tracker**: Visual progress tracker showing completed vs. weekly target hours (*11.5 / 15 hrs*) with interactive `+ Log 1 hr` logging.
  - **Workload Overview & Intensity**: Intensity assessment (*High / Moderate / Light*), daily study distribution bars (Mon–Sun), and AI academic workload recommendations.
- 🌐 **Multilingual Support**: Real-time language switching:
  - English 🇺🇸
  - Español 🇪🇸
  - Français 🇫🇷
  - Deutsch 🇩🇪
  - 中文 🇨🇳
  - हिन्दी 🇮🇳
- 🔔 **Interactive Notification Center**:
  - Live bell icon with unread badge counter.
  - Dropdown drawer with event timestamps, priority levels (Urgent, Success, Info), and "Mark all as read".
  - Instant toast alerts for all major operations.
- 💾 **Data Persistence**:
  - Automatically saves tasks, syllabus documents, study preferences, and language selection in `localStorage`. Work is preserved across page reloads.
- ⏱️ **Academic Focus Pomodoro Timer**:
  - Integrated 25-minute focus session and 5-minute break timer.
- 📑 **Multi-Course Syllabus Upload**: Upload multiple PDF syllabus documents (parsed using PyMuPDF) or paste course text.
- 🧪 **Instant Demo Mode**: "Load Sample Syllabus" pre-loads 3 realistic courses (`CS101`, `MATH201`, `ECON102`) with 8 deliverables.
- ➕ **Add & Search Deliverables**:
  - "+ Add Custom Task" modal to manually input deliverables.
  - Search bar and sorting by date, weight, or course.
- 🔄 **Intelligent Rescheduling**: Offset 2, 3, or 5 days of unavailability (sick, conference, vacation) and dynamically rebalance workload.
- 📥 **Export to Calendar & CSV**: Download standard `.ics` files ready for Google Calendar, Apple Calendar, and Outlook, or export to CSV.

---

## 🚀 Quick Launch (Windows)

### Option A: Web Application (Recommended)
```powershell
# From D:\SyllabusPilot
.\.venv\Scripts\python.exe server.py
```
Open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your browser.

### Option B: Streamlit
```powershell
# From D:\SyllabusPilot
.\.venv\Scripts\streamlit.exe run app.py\app.py
```
Open **[http://localhost:8501](http://localhost:8501)** in your browser.
