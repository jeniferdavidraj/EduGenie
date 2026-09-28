"""
Quiz Module for EduGenie
Generates 3 multiple-choice questions (MCQs) with 4 options each from a given topic or passage.
"""
import re
import json
from gemini_helper import generate_text


def clean_json_block(text: str) -> str:
    """
    Removes Markdown code fences or extra wrappers around JSON.
    """
    text = text.strip()
    # Match ```json ... ``` or ``` ... ```
    match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
    if match:
        return match.group(1).strip()
    
    # Try finding the array bounds [ ... ]
    start = text.find("[")
    end = text.rfind("]")
    if start != -1 and end != -1 and end > start:
        return text[start:end+1].strip()
        
    return text.strip()


def generate_quiz(text: str) -> list:
    """
    Generates 3 multiple choice questions based on the provided topic or passage.
    Returns a Python list of dicts with 'question', 'options', and 'answer'.
    """
    prompt = f"""
You are a quiz generator.

From the following topic or passage, create 3 multiple-choice questions. Each question should include:
- A "question"
- A list of 4 "options"
- A correct "answer" that must exactly match one of the options.

Format your output as **valid JSON**, strictly like this:
[
  {{
    "question": "What is ...?",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

Important: Return ONLY the JSON array. Do not add explanations before or after.

Topic or Passage:
{text}
"""
    try:
        quiz_text = generate_text(prompt)
        cleaned_text = clean_json_block(quiz_text)
        quiz_data = json.loads(cleaned_text)
        
        if isinstance(quiz_data, list) and len(quiz_data) > 0:
            return quiz_data
        else:
            raise ValueError("Parsed JSON is not a valid list of questions.")
    except Exception as e:
        print(f"Error in Quiz generation: {e}")
        return [
            {
                "question": f"Could not generate quiz: {str(e)}",
                "options": ["Please try again with a different topic"],
                "answer": ""
            }
        ]
