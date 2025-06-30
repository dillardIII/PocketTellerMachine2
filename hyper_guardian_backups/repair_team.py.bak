#=== FILE: repair_team.py ===

#Repair Team: Squad of bots assigned to scan, validate, and fix code for autonomy

import os import traceback from syntax_fixer import auto_fix_syntax from code_inspector import inspect_code_quality from phase_status_monitor import set_phase_status

REPO_DIR = "./"  # Adjust if project lives in a subdirectory

REPAIR_LOG = "logs/repair_log.txt"

def list_python_files(): py_files = [] for root, _, files in os.walk(REPO_DIR): for f in files: if f.endswith(".py") and "venv" not in root: py_files.append(os.path.join(root, f)) return py_files

def repair_file(path): try: with open(path, 'r') as file: code = file.read()

print(f"[Repair Bot] 🔍 Inspecting {path}...")
    issues = inspect_code_quality(code)

    if issues:
        print(f"[Repair Bot] ⚠️ Issues found in {path}: {issues}")
        fixed_code = auto_fix_syntax(code, issues)
        with open(path, 'w') as file:
            file.write(fixed_code)
        log_repair(path, issues)
        return True
    else:
        print(f"[Repair Bot] ✅ No issues in {path}")
        return False

except Exception as e:
    error = traceback.format_exc()
    print(f"[Repair Bot] ❌ Error processing {path}: {e}")
    log_repair(path, error)
    return False

def log_repair(file_path, issues): os.makedirs("logs", exist_ok=True) with open(REPAIR_LOG, "a") as log: log.write(f"\n=== {file_path} ===\n{issues}\n")

def run_repair_team(): print("[Repair Squad] 🛠️ Dispatching across codebase...") files = list_python_files() repaired_count = 0

for f in files:
    if repair_file(f):
        repaired_count += 1

print(f"[Repair Squad] ✅ Repairs complete. {repaired_count} file(s) updated.")
set_phase_status("repair_team", True)

if name == "main": run_repair_team()

