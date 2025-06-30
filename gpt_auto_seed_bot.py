from ghost_env import INFURA_KEY, VAULT_ADDRESS
from openai import OpenAI
import os
import time
from datetime import datetime

BRIDGE_DIR = "ptm_bridge_drop"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def auto_seed_loop():
    print("[GPTAutoSeed] 🌱 Auto-seeding loop started.")
    counter = 0
    while True:
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": "Create a short Python script that prints something unique for the PTM empire."}
                ]
            )
            code = response.choices[0].message.content
            filename = f"gpt_seeded_{counter}.py"
            path = os.path.join(BRIDGE_DIR, filename)
            if not os.path.exists(BRIDGE_DIR):
                os.makedirs(BRIDGE_DIR)
            with open(path, "w") as f:
                f.write(code)
            print(f"[GPTAutoSeed] 🌱 Dropped {filename} at {datetime.now()}")
            counter += 1
        except Exception as e:
            print(f"[GPTAutoSeed] ⚠️ Error: {e}")
        time.sleep(60)

def log_event():ef drop_files_to_bridge():