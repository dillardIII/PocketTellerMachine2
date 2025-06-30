from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: continuous_auto_seed_loop.py ===
# 🌱 Continuous GPT Seeder – endlessly writes new code to the bridge

import os, time
from datetime import datetime
from openai import OpenAI

BRIDGE_DIR = "ptm_bridge_drop"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
counter = 0

def generate_file():
    global counter
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": "Write a new creative Python strategy or empire utility."}
        ]
    )
    code = response.choices[0].message.content
    filename = f"gpt_seeded_{counter}.py"
    if not os.path.exists(BRIDGE_DIR):
        os.makedirs(BRIDGE_DIR)
    with open(os.path.join(BRIDGE_DIR, filename), "w") as f:
        f.write(code)
    print(f"[AutoSeeder] 🌱 Dropped {filename} at {datetime.now()}")
    counter += 1

def auto_seed_loop():
    print("[AutoSeeder] 🌱 Continuous GPT seeding started...")
    while True:
        generate_file()
        time.sleep(60)

if __name__ == "__main__":
    auto_seed_loop()

def log_event():ef drop_files_to_bridge():