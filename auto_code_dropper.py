# === FILE: auto_code_dropper.py ===
import os
import time
import json
from openai import OpenAI

PROMPT_DIR = "ptm_strategy_prompts"
BRIDGE_DIR = "ptm_bridge_drop"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_code_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You write standalone Python .py files only."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def drop_code(filename, code):
    if not os.path.exists(BRIDGE_DIR):
        os.makedirs(BRIDGE_DIR)
    path = os.path.join(BRIDGE_DIR, filename)
    with open(path, "w") as f:
        f.write(code)
    print(f"[Dropper] ✅ Dropped: {path}")

def dropper_loop():
    processed = set()
    while True:
        for file in os.listdir(PROMPT_DIR):
            if file.endswith(".txt") and file not in processed:
                with open(os.path.join(PROMPT_DIR, file), "r") as f:
                    prompt = f.read()
                code = generate_code_with_gpt(prompt)
                drop_code(f"autogen_{int(time.time())}.py", code)
                processed.add(file)
        time.sleep(10)

if __name__ == "__main__":
    dropper_loop()