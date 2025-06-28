# === FILE: inspector_bot.py ===
# 🕵️ InspectorBot – Scans PTM for critical files, missing modules, and build consistency

import os
import json
from datetime import datetime

REQUIRED_FILES = [
    "app.py",
    "wallet_manager.py",
    "vault_viewer.html",
    "bridge_drop_agent.py",
    "bridge_pickup_agent.py",
    "bridge_team_launcher.py",
    "autonomy_core.py",
    "ghostforge_core.py",
    "assistant_dispatch.py",
    "wallet_api_routes.py",
    "wallet_ui_display.py",
    "command_listener.py",
    "utils/logger.py",
    "utils/file_utils.py",
    "memory/ghostforge_activity_log.json",
    "vault/wallet_snapshot.json"
]

REPORT_PATH = "inspectorbot_scan_report.json"

class InspectorBot:
    def __init__(self):
        self.report = {
            "timestamp": str(datetime.now()),
            "missing_files": [],
            "found_files": [],
            "total_required": len(REQUIRED_FILES)
        }

    def scan_project(self, base_dir="."):
        for file in REQUIRED_FILES:
            full_path = os.path.join(base_dir, file)
            if os.path.exists(full_path):
                self.report["found_files"].append(file)
            else:
                self.report["missing_files"].append(file)
        self.save_report()

    def save_report(self):
        with open(REPORT_PATH, "w") as f:
            json.dump(self.report, f, indent=2)
        print(f"[InspectorBot] ✅ Scan complete. Report saved to: {REPORT_PATH}")
        print(f"[InspectorBot] 🧾 Missing Files: {len(self.report['missing_files'])}")
        for missing in self.report["missing_files"]:
            print(f"  - {missing}")

# === Entry point ===
if __name__ == "__main__":
    print("[InspectorBot] 🔍 Starting PTM scan...")
    bot = InspectorBot()
    bot.scan_project()