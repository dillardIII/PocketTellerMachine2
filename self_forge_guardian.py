from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os, time
from datetime import datetime
from openai import OpenAI

CRITICAL_FILES = ["main.py", "hyperforge_pipeline.py", "quantum_brain.py", "ghost_memory_matrix.py"]
REBUILD_DIR = "ptm_bridge_drop"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def rebuild_file(name):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": f"Rebuild a complete {name} for PTM empire."}]
    )
    code = response.choices[0].message.content
    path = os.path.join(REBUILD_DIR, f"repaired_{name}")
    with open(path, "w") as f:
        f.write(code)
    print(f"[Guardian] 🛠️ Rebuilt missing {name} -> {path}")

def guardian_loop():
    print("[Guardian] 🛡️ Watching for missing critical files...")
    while True:
        for file in CRITICAL_FILES:
            if not os.path.exists(file):
                print(f"[Guardian] ⚠️ Missing {file}")
                rebuild_file(file)
        time.sleep(45)

if __name__ == "__main__":
    guardian_loop()

def log_event():ef drop_files_to_bridge():