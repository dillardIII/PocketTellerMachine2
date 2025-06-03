# === FILE: replit_squad_manager.py ===
# Supports Replit-side AI autonomy inspections

from cole_logger import log_repair_attempt
from syntax_inspector import check_code_file
from repair_bot_team import auto_patch
from bot_registry import get_all_files

def deploy_replit_ai_review_squad():
    print("[Replit Squad] 🚨 Engaging full file review...")

    files = get_all_files()
    for file in files:
        if not file.endswith(".py"):
            continue  # skip non-Python code

        print(f"[Replit Squad] 🧪 Inspecting: {file}")
        errors = check_code_file(file)

        if errors:
            print(f"[Replit Squad] ❌ Errors found in {file}, sending to repair bots")
            patch_result = auto_patch(file, errors)
            log_repair_attempt(file, patch_result)
        else:
            print(f"[Replit Squad] ✅ {file} is clean")

    print("[Replit Squad] ✅ Review complete")

# This gets called on launcher startup or manually triggered