"""
QnA Module for EduGenie
Handles general knowledge and academic question answering using Google Gemini.
"""
from gemini_helper import generate_text

def answer_question_with_gemini(question: str) -> str:
    """
    Answers an academic or general knowledge question using Google Gemini.
    """
    try:
        prompt = f"You are a helpful educational tutor. Answer the following question clearly, concisely, and accurately:\n\n{question}"
        response_text = generate_text(prompt)
        return response_text.strip()
    except Exception as e:
        return f"⚠ Error in QnA: {e}"
