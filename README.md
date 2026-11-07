# 🎓 SyllabusPilot — AI University Study Planner

**SyllabusPilot** is an executive academic command center built for university students. Upload course syllabus files (PDF, text), let Google Gemini extract deadlines and assessment weights, and generate an optimized weekly study plan with real-time rescheduling, language selection, notifications, and calendar sync.

---

## ✨ Features

- 👤 **Executive Professional Dashboard**:
  - **Personalized Greeting**: Displays the student's name (e.g. *Welcome back, Alex Morgan 👋*) with editable profile.
  - **Current Semester & Academic Progress**: Tracks term progress (*Fall 2026 · Week 9 of 16 · Midterms Period*) with an interactive progress bar showing deliverables completed.
  - **Courses Uploaded Overview**: Shows active course tags extracted from uploaded documents.
  - **Upcoming Assignments & Exams Cockpit**: Prioritizes imminent deadlines with color-coded urgency badges (*"Due in 2 days"*, *"Due Today!"*), exam warnings, weight impacts, and 1-click status completion.
  - **Study Hours Tracker**: Visual progress tracker showing completed vs. weekly target hours with interactive `+ Log 1 hr` logging.
  - **Workload Overview & Dynamic AI Insights**: Evaluates intensity (*High / Moderate / Light*), daily study distribution bars (Mon–Sun), and dynamic AI workload recommendations based on your actual uploaded syllabus.
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
- 📑 **Course Syllabus Upload**: Upload PDF syllabus documents (parsed using PyMuPDF) or paste course text directly.
- 🧪 **Optional Demo Mode**: Built-in test sample data option for quick hackathon demonstrations.
- ➕ **Add & Search Deliverables**:
  - "+ Add Custom Task" modal to manually input deliverables.
  - Search bar and sorting by date, weight, or course.
- 🔄 **Intelligent Rescheduling**: Offset 2, 3, or 5 days of unavailability (sick, conference, vacation) and dynamically rebalance workload.
- 📥 **Export to Calendar & CSV**: Download standard `.ics` files ready for Google Calendar, Apple Calendar, and Outlook, or export to CSV.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.10+, FastAPI, Uvicorn, Streamlit
- **AI Engine**: Google Gemini API (`gemini-flash-latest` via `google-genai` SDK)
- **PDF Extraction**: PyMuPDF (`fitz`)
- **Frontend**: React 18, Tailwind CSS, Lucide Icons
- **Calendar**: iCalendar (`.ics`) format generation

---

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/SyllabusPilot.git
cd SyllabusPilot
```

### 2. Create and activate a virtual environment
```powershell
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API Key
Create a `.env` file in the project root:
```bash
cp .env.example .env
```
Open `.env` and add your Google Gemini API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```
*(Get a key from [Google AI Studio](https://aistudio.google.com/app/apikey))*

---

## 💻 Running the Application

### Option A: Web Application (FastAPI — Recommended)
```powershell
python server.py
```
Open your browser to: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

### Option B: Streamlit Host
```powershell
streamlit run app.py/app.py
```
Open your browser to: **[http://localhost:8501](http://localhost:8501)**

---

## 🔒 Security & Privacy

- `GEMINI_API_KEY` is loaded exclusively from `.env`.
- `.gitignore` prevents `.env`, virtual environments (`.venv/`), and cache files from ever being committed to GitHub.
- Course syllabus data is processed locally and stored in your browser's private `localStorage`.
