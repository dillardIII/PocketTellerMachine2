# === FILE: cole_tools/gpt_advisor.py ===

import os
import json
from datetime import datetime
from cole_logger import log_info

GPT_LOG_FILE = "data/gpt_prompt_log.json"

# === Core GPT Request Function ===
def ask_gpt(prompt):
    """
    Simulates an AI response. Replace with real API later.
    """
    log_info(f"[GPT Advisor] Prompting GPT with: {prompt}")
    return f"Simulated GPT response to: {prompt}"

# === Save GPT Prompt History ===
def log_prompt(prompt, response):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "prompt": prompt,
        "response": response
    }

    history = []
    if os.path.exists(GPT_LOG_FILE):
        try:
            with open(GPT_LOG_FILE, "r") as f:
                history = json.load(f)
        except:
            history = []

    history.append(entry)
    with open(GPT_LOG_FILE, "w") as f:
        json.dump(history[-300:], f, indent=2)

    log_info("[GPT Advisor] Chat logged.")

# === Wrapper for Phase Advice ===
def get_phase_advice(prompt):
    response = ask_gpt(prompt)
    log_prompt(prompt, response)
    return response

# === Wrapper for Task Generation ===
def get_task_list(prompt):
    response = ask_gpt(prompt)
    try:
        return json.loads(response)
    except:
        return []

# === Wrapper for Strategy Notes ===
def get_strategy_note(prompt):
    response = ask_gpt(prompt)
    log_prompt(prompt, response)
    return response

# === CLI Test ===
if __name__ == "__main__":
    advice = get_phase_advice("What should Cole focus on during pre_market?")
    print(advice)