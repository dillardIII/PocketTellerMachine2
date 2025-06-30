# === FILE: ptm_initializer.py ===
# 🧠 PTM Initializer – Handles boot checks, system scans, config load, and persona prep

import os
import time
import json
from pathlib import Path

class PTMInitializer:
    def __init__(self):
        self.status = "uninitialized"
        self.config = {}
        self.personas = []
        self.ready = False

    def boot_sequence(self):
        print("[PTM Initializer] 🚀 Running full boot sequence...")
        self.status = "initializing"

        # Load settings and personas
        self.load_default_config()
        self.register_default_personas()

        # Run diagnostics
        diagnostics = self.run_diagnostics()
        self.ready = diagnostics["pass"]
        self.status = "ready" if self.ready else "fail"

        # Save results to file
        Path("state").mkdir(parents=True, exist_ok=True)
        with open("state/init_report.json", "w", encoding="utf-8") as f:
            json.dump({
                "status": self.status,
                "config": self.config,
                "personas": self.personas,
                "diagnostics": diagnostics
            }, f, indent=2)

        return {
            "status": self.status,
            "config": self.config,
            "personas_loaded": len(self.personas),
            "diagnostics": diagnostics
        }

    def load_default_config(self):
        self.config = {
            "mode": "live",
            "version": "1.0.0",
            "dark_mode": True,
            "log_level": "info"
        }

    def register_default_personas(self):
        self.personas = [
            "Mentor",
            "Mo Cash",
            "Drill Instructor",
            "Strategist",
            "Shadow",
            "Chill Trader",
            "Optimist",
            "OG"
        ]

    def run_diagnostics(self):
        checks = {
            "directories": self.check_directories(),
            "memory_files": self.check_memory_files(),
            "bots_online": self.check_bot_status()
        }
        checks["pass"] = all(checks.values())
        return checks

    def check_directories(self):
        required_dirs = ["state", "memory", "voice_mp3", "logs"]
        print("[Diagnostics] 📁 Checking essential directories...")
        for directory in required_dirs:
            Path(directory).mkdir(parents=True, exist_ok=True)
        return True

    def check_memory_files(self):
        print("[Diagnostics] 🧠 Verifying memory core...")
        try:
            core_file = "memory/ghostshade_core.json"
            if not os.path.exists(core_file):
                with open(core_file, "w", encoding="utf-8") as f:
                    json.dump({"status": "booted", "memory": {}}, f)
            return True
        except Exception as e:
            print(f"[Memory Check] ❌ {e}")
            return False

    def check_bot_status(self):
        print("[Diagnostics] 🤖 Checking AI bots are ready...")
        # Placeholder – Replace with actual status pings
        time.sleep(1)
        return True

    def get_status(self):
        return {
            "status": self.status,
            "ready": self.ready,
            "personas": self.personas
        }