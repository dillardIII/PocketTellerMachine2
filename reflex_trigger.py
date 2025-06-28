# === FILE: reflex_trigger.py ===
# 🧠 Reflex Trigger – Handles file fix requests from log_monitor

from reflex_engine import ReflexEngine
from utils.logger import log_event

def trigger_reflex_fix(error_line):
    print("[ReflexTrigger] 🛠️ Attempting to fix issue from logs...")
    reflex = ReflexEngine()

    # Dumb pattern matching to simulate file repair
    if "app.py" in error_line:
        filename = "app.py"
    elif "main" in error_line:
        filename = "main.py"
    else:
        filename = "unknown_fix.py"

    intent = f"Fix error automatically. Log line: {error_line.strip()}"
    reflex.handle_code_generation({
        "filename": filename,
        "intent": intent,
        "language": "python"
    })

    log_event("ReflexAutoFix", { "filename": filename, "source": "log_monitor" })