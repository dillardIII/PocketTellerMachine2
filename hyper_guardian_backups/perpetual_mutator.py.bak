import os
import random
import time
from auto_file_git_pusher import write_file, git_commit_push

MODULE_DIR = "ptm_modules"
os.makedirs(MODULE_DIR, exist_ok=True)

def mutate_module():
    filename = f"{MODULE_DIR}/mutated_module_{int(time.time())}.py"
    # Dumb mutation for demo – later you can integrate GPT or a local LLM
    content = f"print('[Mutator] 🔥 Mutated at {time.ctime()}')"
    write_file(filename, content)
    git_commit_push(filename, "🔥 Auto-mutation commit")
    print(f"[Mutator] 🚀 Created + pushed: {filename}")

while True:
    mutate_module()
    time.sleep(random.randint(30,90))