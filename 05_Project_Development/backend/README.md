# EduGenie: Google Gemini Powered Learning Assistant 💡

EduGenie is a lightweight AI-powered educational assistant designed for students of all academic levels. Built with **FastAPI** for the backend and a modern **HTML + CSS** frontend, EduGenie leverages Google Gemini generative AI to simplify and personalize learning.

---

## 🚀 Features & Modules

1. **Question & Answer (`/qa`)**:
   - Ask general knowledge or academic questions (e.g., *"Which is the largest ocean?"*).
   - Powered by Google Gemini to return smart, concise answers.

2. **Concept Explanation (`/explain`)**:
   - Simplifies complex topics for school students (e.g., *"Photosynthesis"*, *"Quantum Computing"*).
   - Designed to support local lightweight models (LaMini-Flan-T5-783M) or cloud Gemini.

3. **Text Summarization (`/summarize`)**:
   - Condenses long educational articles, history passages, and notes into key takeaways.

4. **Interactive Quiz Generation (`/quiz`)**:
   - Automatically generates 3 multiple-choice questions (MCQs) with 4 options each from any passage or topic.
   - Includes real-time client-side interactive answer evaluation (`✔ Correct!` / `❌ Incorrect`) and score calculation.

5. **Personalized Learning Roadmap (`/learn/recommendations`)**:
   - Creates a structured curriculum from Beginner to Intermediate and Advanced levels with estimated timelines, recommended books, tutorials, and adaptive study strategies.

---

## 📂 Project Architecture

```
EduGenie/
├── main.py                     # FastAPI application & RESTful routing
├── qna.py                      # Question answering module
├── explanation_module.py       # Concept explanation logic
├── summary_module.py           # Summarization module
├── quiz_module.py              # 3-question MCQ generator with JSON parsing
├── learning_path.py            # Learning roadmap & recommendations
├── gemini_helper.py            # Google Gemini client with automatic model fallback
├── requirements.txt            # Python dependencies
├── .env                        # Gemini API Key configuration
├── templates/
│   └── index.html              # Interactive web frontend
└── static/
    └── style.css               # Modern UI styling & animations
```

---

## 🛠️ Getting Started

### 1. Prerequisites
- Python 3.10+
- Valid Google Gemini API Key

### 2. Installation
Install the dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configure API Key
Create or verify your `.env` file:
```env
GEMINI_API_KEY="your-api-key-here"
```

### 4. Run the Application
Launch the Uvicorn ASGI server:
```bash
uvicorn main:app --reload
```
Or with python launcher:
```bash
py -m uvicorn main:app --reload
```

Navigate to: **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your web browser.

---

## 📡 API Endpoints

| Endpoint | Method | Input | Description |
| :--- | :--- | :--- | :--- |
| `/` | `GET` | — | Renders the EduGenie Web Interface |
| `/qa` | `GET` / `POST` | `question` | Q&A with Google Gemini |
| `/explain` | `POST` | `{"topic": "..."}` | Explains concepts in simple terms |
| `/summarize` | `POST` | `{"text": "..."}` | Summarizes long paragraphs |
| `/quiz` | `POST` | `{"text": "..."}` | Generates 3 MCQs in JSON format |
| `/learn/recommendations` | `GET` / `POST` | `topic` | Comprehensive learning roadmap |
