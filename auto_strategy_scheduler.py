from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: auto_strategy_scheduler.py ===
import os
import time

BRIDGE_PROMPT_DIR = "ptm_strategy_prompts"
if not os.path.exists(BRIDGE_PROMPT_DIR):
    os.makedirs(BRIDGE_PROMPT_DIR)

def log_event(event):
    print(f"[Scheduler] {event}")

def scheduler_loop():
    counter = 0
    while True:
        prompt = f"Build me a Python trading strategy file number {counter} with new logic."
        path = os.path.join(BRIDGE_PROMPT_DIR, f"auto_prompt_{counter}.txt")
        with open(path, "w") as f:
            f.write(prompt)
        log_event(f"⏰ Dropped prompt: {path}")
        counter += 1
        time.sleep(15)

if __name__ == "__main__":
    scheduler_loop()