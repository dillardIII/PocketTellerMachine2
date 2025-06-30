from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: strategy_mutator.py ===
import os
import re
import random
import uuid
from datetime import datetime

MUTATED_DIR = "team_files/Mutated"
os.makedirs(MUTATED_DIR, exist_ok=True)

def mutate_strategy(file_path, bot_name="Mutator"):
    if not os.path.exists(file_path):
        return None

    with open(file_path, "r") as f:
        lines = f.readlines()

    mutated_lines = []
    modified = False

    for line in lines:
        # Mutate numeric thresholds like price, RSI, moving averages
        if re.search(r"price\s*[<>=]+", line):
            line = re.sub(r"(\d{2,3})", lambda m: str(int(m.group(1)) + random.choice([-5, -2, 2, 5])), line)
            modified = True
        elif re.search(r"rsi\s*[<>=]+", line):
            line = re.sub(r"(\d{1,2})", lambda m: str(max(5, min(95, int(m.group(1)) + random.choice([-10, -5, 5, 10])))), line)
            modified = True
        elif re.search(r"MA|ma", line) and re.search(r"\d{2,3}", line):
            line = re.sub(r"(\d{2,3})", lambda m: str(int(m.group(1)) + random.choice([-3, 3, 5, -5])), line)
            modified = True
        elif "risk" in line:
            line = line.replace("0.05", "0.07").replace("0.1", "0.08")
            modified = True
        elif "threshold" in line:
            line = line.replace("0.7", "0.65")
            modified = True
        elif "confidence" in line:
            line = line.replace("0.6", "0.75")
            modified = True

        mutated_lines.append(line)

    if not modified:
        print("[MUTATOR] No changes made to strategy.")
        return None

    base = os.path.basename(file_path).replace(".py", "")
    new_name = f"{bot_name}_mutated_{base}_{uuid.uuid4().hex[:6]}.py"
    new_path = os.path.join(MUTATED_DIR, new_name)

    with open(new_path, "w") as f:
        f.writelines(mutated_lines)

    print(f"[MUTATOR] Created mutated strategy: {new_name}")
    return new_path

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():