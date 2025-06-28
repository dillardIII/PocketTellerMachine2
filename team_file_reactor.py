# === FILE: team_file_reactor.py ===
import os
import importlib.util
import traceback

TEAM_DIR = "team_files"
RESPONSES_DIR = "team_logs/responses"
os.makedirs(RESPONSES_DIR, exist_ok=True)

def scan_and_react(team_name):
    team_folder = os.path.join(TEAM_DIR, team_name)
    if not os.path.exists(team_folder):
        print(f"[REACTOR] No folder for team: {team_name}")
        return

    for fname in os.listdir(team_folder):
        if fname.endswith(".py"):
            full_path = os.path.join(team_folder, fname)
            print(f"[REACTOR] {team_name} reacting to: {fname}")
            try:
                result = _execute_python_file(full_path)
                _log_response(team_name, fname, result)
            except Exception as e:
                _log_response(team_name, fname, f"ERROR: {e}\n{traceback.format_exc()}")

def _execute_python_file(file_path):
    module_name = os.path.splitext(os.path.basename(file_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if hasattr(module, "run_strategy"):
        return module.run_strategy({"test": True})
    else:
        return "[REACTOR] No run_strategy() method found."

def _log_response(team_name, file_name, response):
    log_path = os.path.join(RESPONSES_DIR, f"{team_name}_response_log.txt")
    with open(log_path, "a") as f:
        f.write(f"--- Reaction to {file_name} ---\n")
        f.write(f"{response}\n\n")