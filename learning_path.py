"""
Learning Path Module for EduGenie
Generates personalized, structured learning paths from beginner to advanced levels
with key topics, estimated timelines, resources, and adaptive tips.
"""
from gemini_helper import generate_text


def get_learning_recommendations(topic: str) -> str:
    """
    Generates a personalized, structured learning path for a given topic.
    """
    prompt = f"""You are an AI tutor. The student wants to learn about: {topic}.
Suggest a structured and adaptive learning path including key topics, order of learning, and resources (videos, articles, books, interactive tutorials).
Include beginner, intermediate, and advanced levels with estimated timelines, and conclude with adaptive study tips.

Structure your response clearly with markdown headings, bullet points, and sections like:
- Overview
- I. Beginner Level (Estimated Time, Key Topics, Recommended Resources)
- II. Intermediate Level (Estimated Time, Key Topics, Recommended Resources)
- III. Advanced Level (Estimated Time, Key Topics, Recommended Resources)
- Adaptive Learning Tips
"""
    try:
        response_text = generate_text(prompt)
        if response_text:
            return response_text
        else:
            return "Could not extract content from Gemini response."
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"❌ Error occurred: {str(e)}"
