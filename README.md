# 🤖 AI Autonomous Research Agent

An advanced GenAI-powered Autonomous Research Agent that automatically researches any topic, collects information, generates reports, creates charts, and exports the results as PDF and PowerPoint presentations.

---

## 🚀 Project Overview

This project uses multiple AI agents to automate the research process. The user enters a research topic, and the system performs web research, analyzes the collected information, generates a professional report, creates visual charts, and exports the results into PDF and PPT formats.

---

## ✨ Features

- AI-powered autonomous research
- Multi-agent workflow
- Automatic report generation
- PDF export
- PowerPoint generation
- Chart generation
- Modern web interface
- Modular architecture
---

# 🏗️ System Architecture

```
User
   │
   ▼
Research Agent
   │
   ▼
Web Search Agent
   │
   ▼
Content Collection Agent
   │
   ▼
Writer Agent
   │
   ▼
Chart Generator
   │
   ▼
PDF Generator
   │
   ▼
PowerPoint Generator
```
---

# 📁 Project Structure

```
AI_Autonomous_Research_Agent/
│
├── agents/
│   ├── planner.py
│   ├── researcher.py
│   ├── writer.py
│   ├── image_agent.py
│   ├── chart_generator.py
│   ├── pdf_agent.py
│   └── ppt_agent.py
│
├── backend/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── charts/
│
├── docs/
│   └── images/
│
├── images/
│
├── reports/
│
├── ppts/
│
├── README.md
├── requirements.txt
└── LICENSE
```
---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/ramprasad-988/Autonomous_Research_Agent.git
```

## 2. Navigate to the Project

```bash
cd Autonomous_Research_Agent
```

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

## 4. Activate the Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```
---

# ▶️ Running the Project

## Start the Backend

```bash
python backend/main.py
```

## Start the Frontend

```bash
streamlit run frontend/app.py
```

## Open in Browser

```
http://localhost:8501
```

Enter a research topic and the system will automatically:

- Generate a research plan
- Search for information
- Write the report
- Generate charts
- Create images
- Generate a professional PDF
- Generate a PowerPoint presentation