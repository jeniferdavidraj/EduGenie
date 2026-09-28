from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

# Module imports matching project specification
from qna import answer_question_with_gemini
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(
    title="EduGenie: Google Gemini Powered Learning Assistant",
    description="An AI-powered educational assistant for students of all academic levels.",
    version="1.0.0"
)

# Enable CORS for universal accessibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directory configurations
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

STATIC_DIR.mkdir(parents=True, exist_ok=True)
TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    """
    Renders the EduGenie frontend web interface.
    """
    return templates.TemplateResponse(request=request, name="index.html")


# ----------------------------------------------------
# 1. Q&A Module (/qa)
# ----------------------------------------------------
@app.get("/qa")
async def answer_question(question: str = Query(...)):
    """
    Q&A - GET API using Gemini
    """
    answer = answer_question_with_gemini(question)
    return {"answer": answer}


@app.post("/qa")
async def answer_question_post(request: Request):
    """
    Q&A - POST API alternative
    """
    data = await request.json()
    question = data.get("question") or data.get("prompt")
    if not question:
        return JSONResponse(content={"error": "Please provide a question."}, status_code=400)
    answer = answer_question_with_gemini(question)
    return {"answer": answer}


@app.post("/ask")
async def ask_alias(request: Request):
    """
    Legacy /ask endpoint compatibility
    """
    data = await request.json()
    question = data.get("question") or ""
    answer = answer_question_with_gemini(question)
    return {"question": question, "answer": answer}


# ----------------------------------------------------
# 2. Explanation Module (/explain)
# ----------------------------------------------------
@app.post("/explain")
async def explain_api(request: Request):
    """
    Explanation - POST API
    """
    data = await request.json()
    topic = data.get("topic")
    if not topic:
        return JSONResponse(content={"error": "Please provide a topic."}, status_code=400)
    explanation = explain_topic(topic)
    return {"topic": topic, "explanation": explanation}


@app.get("/explain")
async def explain_get(topic: str = Query(...)):
    explanation = explain_topic(topic)
    return {"topic": topic, "explanation": explanation}


# ----------------------------------------------------
# 3. Summarization Module (/summarize)
# ----------------------------------------------------
@app.post("/summarize")
async def summarize_api(request: Request):
    """
    Summarization - POST API
    """
    data = await request.json()
    text = data.get("text")
    if not text:
        return JSONResponse(content={"error": "Please provide text to summarize."}, status_code=400)
    summary = summarize_text(text)
    return {"summary": summary}


@app.get("/summarize")
async def summarize_get(text: str = Query(...)):
    summary = summarize_text(text)
    return {"summary": summary}


# ----------------------------------------------------
# 4. Quiz Generation Module (/quiz)
# ----------------------------------------------------
@app.post("/quiz")
async def quiz_api(request: Request):
    """
    Quiz Generation - POST API
    """
    data = await request.json()
    text = data.get("text")
    if not text:
        return JSONResponse(content={"error": "Please provide text for quiz."}, status_code=400)
    quiz = generate_quiz(text)
    print("Generated quiz:", quiz)  # DEBUG
    return JSONResponse(content={"quiz": quiz})


@app.get("/quiz")
async def quiz_get(text: str = Query(...)):
    quiz = generate_quiz(text)
    return JSONResponse(content={"quiz": quiz})


# ----------------------------------------------------
# 5. Learning Recommendations Module (/learn/recommendations)
# ----------------------------------------------------
@app.get("/learn/recommendations")
async def learning_recommendation_api(topic: str = Query(...)):
    """
    Learning Recommendations - GET API
    """
    recommendation = get_learning_recommendations(topic)
    return {"topic": topic, "recommendation": recommendation}


@app.post("/learn/recommendations")
async def learning_recommendation_post(request: Request):
    data = await request.json()
    topic = data.get("topic")
    if not topic:
        return JSONResponse(content={"error": "Please provide a topic."}, status_code=400)
    recommendation = get_learning_recommendations(topic)
    return {"topic": topic, "recommendation": recommendation}