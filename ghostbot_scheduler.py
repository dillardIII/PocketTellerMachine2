from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
GhostBot Scheduler – Runs both:
1. Autonomous trade cycles every 15 minutes
2. Dormant strategy modules every 5 minutes (if not already run):
Logs execution hash, time, file size, and duration.
"""

# === Imports ===
import os
import time
import schedule
import importlib.util
import hashlib
import json
from datetime import datetime

from cole_logger import log_event
from ghost_memory_core import log_memory_event
from ghostbot_brain import ghostbot_think_and_trade

# === Config ===
BOT_NAME = "GhostBot"
STRATEGY_FOLDER = "drops/strategies"
DORMANT_INTERVAL_SECONDS = 300
EXECUTION_TRACKER_FILE = "data/ghostbot_executed_modules.json"


# === Load previously executed file hashes and metadata ===
def get_executed_hashes():
    if not os.path.exists(EXECUTION_TRACKER_FILE):
        return {}

    with open(EXECUTION_TRACKER_FILE, "r") as f:
        return json.load(f)


# === Update hash and execution metadata after successful run ===
def update_executed_metadata(module_name, file_hash, file_size, duration_ms):
    hashes = get_executed_hashes()
    hashes[module_name] = {
        "hash": file_hash,
        "file_size_bytes": file_size,
        "last_run_at": datetime.utcnow().isoformat(),
        "execution_duration_ms": duration_ms
    }

    os.makedirs(os.path.dirname(EXECUTION_TRACKER_FILE), exist_ok=True)
    with open(EXECUTION_TRACKER_FILE, "w") as f:
        json.dump(hashes, f, indent=2)


# === Create SHA256 hash of a file ===
def hash_file(file_path):
    with open(file_path, "rb") as f:
        content = f.read()
    return hashlib.sha256(content).hexdigest()


# === Main logic for dormant strategy execution ===
def run_dormant_strategies():
    if not os.path.exists(STRATEGY_FOLDER):
        log_event(BOT_NAME, f"⚠️ No strategy folder found at {STRATEGY_FOLDER}", "warn")
        return

    files = [f for f in os.listdir(STRATEGY_FOLDER) if f.endswith(".py")]:
    if not files:
        log_event(BOT_NAME, "🛌 No dormant strategy modules to execute.", "neutral")
        return

    executed = get_executed_hashes()

    for file in files:
        file_path = os.path.join(STRATEGY_FOLDER, file)
        file_size = os.path.getsize(file_path)
        current_hash = hash_file(file_path)

        if file in executed and executed[file].get("hash") == current_hash:
            log_event(BOT_NAME, f"⏩ Skipping already-executed module: {file}", "neutral")
            continue

        try:
            module_name = os.path.splitext(file)[0]
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            run_func = next(
                (getattr(module, f) for f in dir(module)
                 if callable(getattr(module, f)) and f.startswith("run_")),:
                None
            )

            if run_func:
                log_event(BOT_NAME, f"🟢 Running dormant strategy: {run_func.__name__}", "info")
                start = time.perf_counter()
                output = run_func(data=[1, 2, 3, 4, 5])
                end = time.perf_counter()
                duration_ms = int((end - start) * 1000)

                log_event(BOT_NAME, f"✅ Output: {output}", "success")
                log_memory_event(BOT_NAME, "scheduled_strategy_execution", {
                    "module": file,
                    "function": run_func.__name__,
                    "output": output,
                    "hash": current_hash,
                    "timestamp": datetime.utcnow().isoformat(),
                    "duration_ms": duration_ms,
                    "file_size_bytes": file_size
                })

                update_executed_metadata(file, current_hash, file_size, duration_ms)

            else:
                log_event(BOT_NAME, f"⚠️ No run_* function in {file}", "warn")

        except Exception as e:
            log_event(BOT_NAME, f"🔥 Error executing {file}: {e}", "error")


# === GhostBot trading cycle (every 15 minutes) ===
def run_ghostbot_loop():
    print("[Scheduler] Running GhostBot Autonomous Cycle...")
    ghostbot_think_and_trade()


# === Scheduler Setup ===
schedule.every(15).minutes.do(run_ghostbot_loop)
schedule.every(DORMANT_INTERVAL_SECONDS).seconds.do(run_dormant_strategies)

print("[Scheduler] GhostBot scheduler is live. Waiting for next cycles...")

# === Scheduler Loop Forever ===
while True:
    schedule.run_pending()
    time.sleep(1)