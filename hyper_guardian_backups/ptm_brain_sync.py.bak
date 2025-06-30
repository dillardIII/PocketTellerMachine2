# === FILE: ptm_brain_sync.py ===

import json, os, time
from datetime import datetime
from ptm_message_relay import send_message

# === Constants ===
LOG_DIR = "logs/"
MEMORY_FILE = "memory/ptm_brain.json"
WATCH_FILES = [
    "strategy_reason_log.json",
    "cole_tasks.json",
    "self_commands_log.json",
    "intel_log.json",
    "bridge_sync.json"
]

# === JSON Loaders and Memory Writers ===
def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ Failed to read {path}: {e}")
        return None

def update_memory(memory, tag, data):
    if tag not in memory:
        memory[tag] = []
    memory[tag].append(data)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

# === Real-time Tag Classifier and Streamer ===
def tag_and_stream(file, entry):
    if "task" in entry.get("type", "").lower():
        send_message("PTM_Brain", "Cole", "new_task", entry)
    elif "strategy" in file:
        send_message("PTM_Brain", "Strategist", "analyze_strategy", entry)
    elif "intel" in file:
        send_message("PTM_Brain", "Malik", "intel_drop", entry)
    elif "command" in file:
        send_message("PTM_Brain", "Mentor", "review_command", entry)

# === Live Memory Sync Loop ===
def run_brain_sync():
    print("🧠 [PTM_Brain] Memory sync online...")
    brain_memory = {}

    file_positions = {f: 0 for f in WATCH_FILES}

    while True:
        for filename in WATCH_FILES:
            path = os.path.join(LOG_DIR, filename)
            if not os.path.exists(path):
                continue

            try:
                with open(path, "r") as f:
                    f.seek(file_positions[filename])
                    lines = f.readlines()
                    file_positions[filename] = f.tell()

                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                        tag_and_stream(filename, entry)
                        update_memory(brain_memory, filename, entry)
                    except Exception as e:
                        print(f"❌ Bad entry in {filename}: {e}")

            except Exception as e:
                print(f"⚠️ Error reading {filename}: {e}")

        save_memory(brain_memory)
        time.sleep(3)

# === Recon Drop Sync (Single Entry Writer) ===
def sync_recon_result(agent_name, result_data):
    """
    Syncs recon result into ptm_brain.json under the recon_logs key.
    """
    brain_path = MEMORY_FILE
    os.makedirs(os.path.dirname(brain_path), exist_ok=True)

    if not os.path.exists(brain_path):
        ptm_brain = {}
    else:
        with open(brain_path, "r") as f:
            try:
                ptm_brain = json.load(f)
            except json.JSONDecodeError:
                ptm_brain = {}

    if "recon_logs" not in ptm_brain:
        ptm_brain["recon_logs"] = []

    result_data["agent"] = agent_name
    result_data["timestamp"] = result_data.get("timestamp", datetime.utcnow().isoformat() + "Z")

    ptm_brain["recon_logs"].append(result_data)

    with open(brain_path, "w") as f:
        json.dump(ptm_brain, f, indent=2)

    print(f"[PTM BRAIN SYNC] Logged recon from {agent_name}")

# === Entry Point ===
if __name__ == "__main__":
    run_brain_sync()