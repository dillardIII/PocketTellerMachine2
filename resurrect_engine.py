# === FILE: resurrect_engine.py ===
import os
import json
import uuid
from datetime import datetime
from shutil import copyfile

CEMETERY_DIR = "evolution/mutation_cemetery"
RESURRECTED_DIR = "team_files/Resurrected"
RESURRECTION_LOG = os.path.join(CEMETERY_DIR, "resurrection_log.json")

os.makedirs(CEMETERY_DIR, exist_ok=True)
os.makedirs(RESURRECTED_DIR, exist_ok=True)

def log_resurrection(original_file, new_file, reason="experimental revival"):
    if not os.path.exists(RESURRECTION_LOG):
        with open(RESURRECTION_LOG, "w") as f:
            json.dump([], f, indent=2)

    with open(RESURRECTION_LOG, "r") as f:
        log = json.load(f)

    log.append({
        "original": os.path.basename(original_file),
        "resurrected": os.path.basename(new_file),
        "timestamp": datetime.utcnow().isoformat(),
        "reason": reason
    })

    with open(RESURRECTION_LOG, "w") as f:
        json.dump(log, f, indent=2)

    print(f"[RESURRECTED] {original_file} -> {new_file} | Reason: {reason}")

def revive_random_strategy():
    candidates = [f for f in os.listdir(CEMETERY_DIR) if f.endswith(".py")]
    if not candidates:
        print("🪦 No bodies in the cemetery to revive.")
        return None

    original = os.path.join(CEMETERY_DIR, random.choice(candidates))
    base = os.path.basename(original).replace(".py", "")
    new_name = f"{base}_revived_{uuid.uuid4().hex[:6]}.py"
    new_path = os.path.join(RESURRECTED_DIR, new_name)

    copyfile(original, new_path)
    log_resurrection(original, new_path)

    return new_path

if __name__ == "__main__":
    revive_random_strategy()