# === strategy_optimizer.py ===
import random
import json
import os
from datetime import datetime
from cole_memory_brain import log_memory_event
from cole_code_writer import cole_write_code

OPTIMIZER_LOG = "logs/strategy_optimizer_log.json"

def optimize_strategy_parameters(strategy_name):
    # Simulate a parameter change (later this will parse actual code logic)
    new_version = f"{strategy_name}_v{random.randint(2, 9)}"
    description = f"Tuning {strategy_name} parameters for better performance."

    print(f"[Optimizer] Creating optimized version: {new_version}")
    log_memory_event("strategy_tuning", {
        "original": strategy_name,
        "tuned_version": new_version,
        "timestamp": datetime.now().isoformat(),
        "description": description
    })

    try:
        code = cole_write_code(description)
        filename = f"{new_version}.py"
        folder = "optimized_strategies"
        os.makedirs(folder, exist_ok=True)

        with open(os.path.join(folder, filename), "w") as f:
            f.write(code)

        log_optimizer_event({
            "strategy": strategy_name,
            "new_version": new_version,
            "filename": filename,
            "timestamp": datetime.now().isoformat()
        })

        return new_version
    except Exception as e:
        print(f"[Optimizer ERROR] {e}")
        return None

def log_optimizer_event(entry):
    os.makedirs("logs", exist_ok=True)
    if os.path.exists(OPTIMIZER_LOG):
        with open(OPTIMIZER_LOG, "r") as f:
            try:
                data = json.load(f)
            except:
                data = []
    else:
        data = []
    data.append(entry)
    with open(OPTIMIZER_LOG, "w") as f:
        json.dump(data, f, indent=2)