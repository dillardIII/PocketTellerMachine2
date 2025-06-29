# === FILE: idle_mutator.py ===
# 🌱 Idle Mutator – generates new salvage, brute or scan tasks when idle

import time
import random
import os

def mutate_idle():
    print("[IdleMutator] 🌱 Running idle mutation cycles.")
    while True:
        if random.random() > 0.7:
            task_file = f"ptm_modules/auto_task_{int(time.time())}.py"
            with open(task_file, "w") as f:
                f.write(f"# Auto-generated salvage scan\nprint('Running auto-task at {time.ctime()}')")
            print(f"[IdleMutator] 🧬 Generated new task: {task_file}")
        time.sleep(20)

if __name__ == "__main__":
    mutate_idle()