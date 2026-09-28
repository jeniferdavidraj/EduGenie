import os
import time
from pathlib import Path
from dotenv import load_dotenv

# Try loading .env from current working directory or parent directories
env_paths = [
    Path(".env"),
    Path(__file__).parent / ".env",
    Path(__file__).parent.parent / ".env",
    Path(__file__).parent.parent.parent / ".env",
]
for ep in env_paths:
    if ep.exists():
        load_dotenv(ep)
        break

API_KEY = os.getenv("GEMINI_API_KEY")

# Supported models list for automatic fallback if high demand or quota reached
MODELS_TO_TRY = [
    os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
    "gemini-flash-latest",
    "gemma-4-26b-a4b-it",
    "gemma-4-31b-it",
]

_client = None

def get_gemini_client():
    global _client
    if _client is not None:
        return _client
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set in environment or .env file.")
    
    from google import genai
    _client = genai.Client(api_key=api_key)
    return _client

def generate_text(prompt: str) -> str:
    """
    Generates text using Google Gemini with intelligent model fallback.
    """
    client = get_gemini_client()
    last_error = None
    
    for model_name in MODELS_TO_TRY:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )
            if response and hasattr(response, "text") and response.text:
                return response.text.strip()
            elif response and hasattr(response, "parts") and response.parts:
                return response.parts[0].text.strip()
        except Exception as e:
            last_error = e
            # Small delay before trying fallback model if needed
            time.sleep(0.5)
            continue
            
    if last_error:
        raise last_error
    return ""
