# === FILE: cole_multi_gpt_router.py ===

from cole_openai_bridge import ask_gpt
from cole_gpt_memory import log_gpt_prompt

# === GPT Persona Wrappers ===

def ask_mentor(prompt):
    full_prompt = (
        "You are a calm and experienced trading mentor. "
        "Write Python trading strategies that are safe, clear, and easy to understand. "
        f"Request: {prompt}"
    )
    response = ask_gpt(full_prompt)
    log_gpt_prompt(full_prompt, response, persona="MentorGPT")
    return response

def ask_hustler(prompt):
    full_prompt = (
        "You are an aggressive trader who looks for quick flips and high upside. "
        "Your Python trading strategies use bold signals, short-term momentum, and volume spikes. "
        f"Request: {prompt}"
    )
    response = ask_gpt(full_prompt)
    log_gpt_prompt(full_prompt, response, persona="HustlerGPT")
    return response

def ask_strategist(prompt):
    full_prompt = (
        "You are a tactical strategist who writes well-balanced Python trading code. "
        "You favor technical indicators, clear risk controls, and edge stacking. "
        f"Request: {prompt}"
    )
    response = ask_gpt(full_prompt)
    log_gpt_prompt(full_prompt, response, persona="StrategistGPT")
    return response