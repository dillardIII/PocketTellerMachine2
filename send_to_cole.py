from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from datetime import datetime
import openai

MEMORY_FILE = "data/cole_memory.json"
RESULTS_FILE = "data/cole_results.json"
PATTERNS_FILE = "data/cole_patterns.json"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY")

client = openai.OpenAI(api_key=OPENAI_API_KEY)

# === LOG THOUGHT ===
def log_brain_thought(prompt, response):
    entry = {
        "timestamp": str(datetime.now()),
        "prompt": prompt,
        "response": response
    }
    os.makedirs("data", exist_ok=True)
    if os.path.exists(MEMORY_FILE):
        memory = json.load(open(MEMORY_FILE, "r"))
    else:
        memory = []
    memory.append(entry)
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)
    print("[MEMORY LOGGED]:", prompt[:50], "...")

# === BRAIN THINK ===
def cole_think(prompt):
    try:
        print("[THINKING]:", prompt)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You're an elite trading AI who analyzes results and improves strategy logic."},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response.choices[0].message.content.strip()
        log_brain_thought(prompt, answer)
        return answer
    except Exception as e:
        print("[THINKING ERROR]:", str(e))
        return None

def log_event():ef drop_files_to_bridge():