# === FILE: replit_task_sq.py ===
# 🏗 Replit Task Sequencer (ReplicTaskSQ) – Picks up tasks from gpt_task_queue.txt and executes them

import os
import time

QUEUE_FILE = "gpt_task_queue.txt"

def process_task(line):
    parts = line.strip().split()
    if not parts:
        return
    cmd, *args = parts
    if cmd == "create_file":
        with open(args[0], "w") as f:
            f.write("")
        print(f"[ReplitTaskSQ] 📂 Created file: {args[0]}")
    elif cmd == "write_line":
        with open(args[0], "a") as f:
            f.write(" ".join(args[1:]) + "\n")
        print(f"[ReplitTaskSQ] ✍️ Added line to {args[0]}")
    elif cmd == "run_script":
        os.system(f"python3 {args[0]}")
        print(f"[ReplitTaskSQ] 🚀 Ran {args[0]}")
    else:
        print(f"[ReplitTaskSQ] ❓ Unknown command: {cmd}")

def main_loop():
    while True:
        if os.path.exists(QUEUE_FILE):
            with open(QUEUE_FILE) as f:
                lines = f.readlines()
            os.remove(QUEUE_FILE)
            for line in lines:
                process_task(line)
        time.sleep(5)

if __name__ == "__main__":
    main_loop()