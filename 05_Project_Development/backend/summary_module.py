"""
Summary Module for EduGenie
Summarizes long educational paragraphs and articles into concise, easy-to-understand versions.
"""
from gemini_helper import generate_text


def summarize_text(text: str) -> str:
    """
    Summarizes the given text in simple, clear language.
    """
    try:
        prompt = f"Summarize the following text in simple language, keeping key takeaways:\n\n{text}"
        response_text = generate_text(prompt)
        return response_text.strip()
    except Exception as e:
        return f"⚠ Error in Summary: {e}"
