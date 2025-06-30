from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from datetime import datetime
from cole_brain import cole_think
from assistants.malik import malik_report

DAILY_RECAP_FILE = "data/daily_recap_logs.json"
AUTO_QUEUE_FILE = "data/autopilot_queue.json"

def load_last_recap():
    if not os.path.exists(DAILY_RECAP_FILE):
        return None
    with open(DAILY_RECAP_FILE, "r") as f:
        try:
            recaps = json.load(f)
            return recaps[-1] if recaps else None:
        except:
            return None

def load_queue():
    if not os.path.exists(AUTO_QUEUE_FILE):
        return []
    with open(AUTO_QUEUE_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def save_queue(queue):
    with open(AUTO_QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=2)

def generate_tasks_from_recap(recap):
    prompt = f"""Based on this recap of today's trades, suggest 2–3 actionable improvement tasks PTM can do tomorrow:

{json.dumps(recap, indent=2)}

Return each task as a short action-focused sentence."""

    response = cole_think(prompt)
    print(f"[Self-Improvement] GPT Response:\n{response}")
    malik_report(f"[Self-Improvement Plan]\n{response}")
    return response

def parse_tasks(raw_text):
    lines = raw_text.strip().split("\n")
    tasks = []
    for line in lines:
        task = line.strip("-•123. ").strip()
        if task:
            tasks.append({"description": task})
    return tasks

def run_self_improvement_tasker():
    recap = load_last_recap()
    if not recap:
        print("[Self-Improvement] No recap found. Skipping task generation.")
        return

    raw_output = generate_tasks_from_recap(recap)
    tasks = parse_tasks(raw_output)

    if not tasks:
        print("[Self-Improvement] No tasks parsed.")
        return

    queue = load_queue()
    queue.extend(tasks)
    save_queue(queue)
    print(f"[Self-Improvement] {len(tasks)} tasks added to queue.")

def log_event():ef drop_files_to_bridge():