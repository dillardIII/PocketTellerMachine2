from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import time
import json
import importlib.util
from datetime import datetime
from assistants.malik import malik_report

WATCH_DIR = "cole_generated_code"
PROCESSED_LOG = "data/ghost_injected_backtest_log.json"
os.makedirs("data", exist_ok=True)

# === Load Tracking Log ===
def load_processed_log():
    if os.path.exists(PROCESSED_LOG):
        with open(PROCESSED_LOG, "r") as f:
            return set(json.load(f))
    return set()

# === Save Updated Log ===
def save_processed_log(log_set):
    with open(PROCESSED_LOG, "w") as f:
        json.dump(list(log_set), f, indent=2)

# === Attempt to Import & Run Backtest ===
def run_injected_backtest(file_path):
    try:
        print(f"[Ghost Backtester] Backtesting {file_path}")
        module_name = os.path.splitext(os.path.basename(file_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "cole_generated_function"):
            result = module.cole_generated_function()
            print(f"[Ghost Backtester] Result: {result}")
            malik_report(f"[Backtest] {module_name} executed: {result}")
        else:
            print("[Ghost Backtester] No callable `cole_generated_function()` found.")
            malik_report(f"[Backtest] {module_name} skipped (no entry function).")

    except Exception as e:
        print(f"[Ghost Backtester] Error running {file_path}: {str(e)}")
        malik_report(f"[Backtest Error] {file_path}: {str(e)}")

# === Watch Loop ===
def watch_and_backtest():
    print("[Ghost Backtester] Watching for new generated code...")
    seen = load_processed_log()

    while True:
        try:
            for filename in os.listdir(WATCH_DIR):
                if not filename.endswith(".py"):
                    continue
                full_path = os.path.join(WATCH_DIR, filename)
                if full_path not in seen:
                    run_injected_backtest(full_path)
                    seen.add(full_path)
                    save_processed_log(seen)
            time.sleep(10)
        except Exception as e:
            print(f"[Ghost Backtester] Loop Error: {str(e)}")
            time.sleep(10)

# === CLI Trigger ===
if __name__ == "__main__":
    watch_and_backtest()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():