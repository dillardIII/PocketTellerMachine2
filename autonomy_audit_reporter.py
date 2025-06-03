# === FILE: autonomy_audit_reporter.py ===
# Reports system readiness and autonomy progress

import os

def report_autonomy_status():
    print("[Audit] 🧾 Checking for autonomy readiness...")

    required_files = [
        "autonomy_launcher.py",
        "cole_loop_controller.py",
        "gpt_self_command_engine.py",
        "ai_repair_bot.py",
        "replit_team_commander.py",
        "system_logger.py",
        "ptm_gpt_agent.py",
        "cole_brain.py"
        # Add more if needed
    ]

    existing = [f for f in required_files if os.path.exists(f)]
    percent = round((len(existing) / len(required_files)) * 100, 2)

    print(f"[Audit] ✅ Autonomy readiness: {percent}%")
    if percent >= 95:
        print("[Audit] 🚀 PTM is ready to activate autonomy mode!")
    else:
        print(f"[Audit] ⏳ {len(required_files) - len(existing)} files missing")