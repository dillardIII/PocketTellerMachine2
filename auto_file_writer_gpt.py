# 🚀 AutoFileWriterGPT – writes commands into gpt_task_queue.txt forever
# 🧬 Feeds the task queue to evolve your empire with zero manual input

import time
import random

QUEUE_FILE = "gpt_task_queue.txt"

MODULE_TEMPLATES = [
    ("create_file", "autogen_{}.py"),
    ("write_line", "{} print('[AutoEmpire] 🔥 Hello from evolving empire')"),
    ("run_script", "{}")
]

def queue_task(line):
    with open(QUEUE_FILE, "a") as f:
        f.write(line + "\n")
    print(f"[AutoFileWriterGPT] 📝 Queued: {line}")

def auto_writer_loop():
    while True:
        timestamp = int(time.time())
        module_name = f"autogen_{timestamp}.py"

        # Always create file first
        queue_task(f"create_file {module_name}")
        # Then add simple print line
        queue_task(f"write_line {module_name} print('[AutoEmpire] 🔥 Running at {timestamp}')")
        # Then run it
        queue_task(f"run_script {module_name}")

        wait_time = random.choice([30, 60, 90])
        print(f"[AutoFileWriterGPT] ⏳ Sleeping {wait_time}s before next cycle...")
        time.sleep(wait_time)

if __name__ == "__main__":
    print("[AutoFileWriterGPT] 🚀 Starting perpetual auto task feeder...")
    auto_writer_loop()