"""
Explanation Module for EduGenie
Uses LaMini-Flan-T5-783M (local lightweight model) if available,
with graceful fallback to Google Gemini for reliable execution.
"""
from gemini_helper import generate_text

explain_tokenizer = None
explain_model = None
local_model_loaded = False

try:
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
    import torch
    # Note: To enable local LaMini-Flan-T5 model, install transformers & torch
    # and uncomment the initialization below if pre-downloaded:
    # explain_tokenizer = AutoTokenizer.from_pretrained("MBZUAI/LaMini-Flan-T5-783M")
    # explain_model = AutoModelForSeq2SeqLM.from_pretrained("MBZUAI/LaMini-Flan-T5-783M")
    # local_model_loaded = True
except Exception:
    local_model_loaded = False


def explain_topic(topic: str) -> str:
    """
    Explains a concept in a simple and clear way for a school student.
    """
    input_text = f"Explain the concept of '{topic}' in a simple and clear way for a school student."
    
    if local_model_loaded and explain_tokenizer is not None and explain_model is not None:
        try:
            inputs = explain_tokenizer(input_text, return_tensors="pt")
            outputs = explain_model.generate(
                **inputs,
                max_new_tokens=150,
                temperature=0.7,
                top_k=50,
                top_p=0.95,
                do_sample=True
            )
            explanation = explain_tokenizer.decode(outputs[0], skip_special_tokens=True)
            return explanation
        except Exception as e:
            print(f"Local model generation failed: {e}. Falling back to Gemini.")
    
    # Gemini fallback
    try:
        return generate_text(input_text)
    except Exception as e:
        return f"⚠ Error in Explanation: {e}"
