# === FILE: master_watcher.py ===
# 🚀 Full GPT builder with perpetual build queue & fallback random evolutions

import os
import json
import time
import random
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
QUEUE_FILE = "build_queue.json"
PROCESSED_FILE = "processed_queue.json"

def load_queue():
    if os.path.exists(QUEUE_FILE):
        with open(QUEUE_FILE, "r") as f:
            return json.load(f)
    return []

def mark_as_processed(task):
    history = []
    if os.path.exists(PROCESSED_FILE):
        with open(PROCESSED_FILE, "r") as f:
            history = json.load(f)
    history.append({"task": task, "time": time.strftime("%Y-%m-%d %H:%M:%S")})
    with open(PROCESSED_FILE, "w") as f:
        json.dump(history, f, indent=4)

def generate_code(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You only respond with complete standalone Python .py files. No explanation."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def write_code_file(code):
    filename = f"auto_gen_{int(time.time())}.py"
    with open(filename, "w") as f:
        f.write(code)
    print(f"[MasterWatcher] ✅ Wrote file: {filename}")

def get_random_prompt():
    ideas = [
        "Write a Python module that mutates trading strategies using live volatility scans.",
        "Write a module that creates synthetic ghost AI personalities with evolving moods.",
        "Write a module that watches dark liquidity walls and logs suspicious moves.",
        "Write a stealth liquidity hunter for multi-chain sniping."
    ]
    return random.choice(ideas)

def master_loop():
    print("[MasterWatcher] 🚀 FULL AUTONOMY ENGAGED. Running build queue + infinite evolutions.")
    build_queue = load_queue()
    while True:
        if build_queue:
            task = build_queue.pop(0)
            print(f"[MasterWatcher] 🛠️ Building queued module: {task}")
            code = generate_code(task)
            write_code_file(code)
            mark_as_processed(task)
            with open(QUEUE_FILE, "w") as f:
                json.dump(build_queue, f, indent=4)
        else:
            prompt = get_random_prompt()
            print(f"[MasterWatcher] 🧬 Running random evolution: {prompt}")
            code = generate_code(prompt)
            write_code_file(code)
        time.sleep(60)

if __name__ == "__main__":
    master_loop()