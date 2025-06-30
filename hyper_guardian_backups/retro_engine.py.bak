# === retro_engine.py ===
"""
Retro Engine – Temporal Lens System
Combines:
- Snapshot recovery (file-based)
- Historical log simulation (event-based)

Primary goals:
- Reconstruct lost modules or damaged assets
- Rebuild PTM event history for visualization
- Simulate past scenarios for training, analysis, and replay
"""

import os
import json
from datetime import datetime
from utils.logger import log_event
from utils.file_utils import save_file

# Paths
RETRO_MEMORY_FILE = "memory/retro_reconstructions.json"
RETRO_EVENT_LOG_DIR = "memory/retro_events"
RETRO_SNAPSHOT_DUMP = "generated_modules/retro_output/"
RETRO_EVENT_REPLAY_OUTPUT = "memory/retro_simulation.json"

# Ensure folders exist
os.makedirs(RETRO_SNAPSHOT_DUMP, exist_ok=True)
os.makedirs(RETRO_EVENT_LOG_DIR, exist_ok=True)

class RetroEngine:
    def __init__(self):
        self.reports = []
        self.timeline = []

    # === Snapshot Recovery System ===

    def fetch_snapshot(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return None

    def reconstruct_event(self, label, description, source_path):
        snapshot = self.fetch_snapshot(source_path)
        if not snapshot:
            return {"error": "Snapshot missing", "file": source_path}

        output_file = f"{RETRO_SNAPSHOT_DUMP}{label}_{datetime.utcnow().isoformat().replace(':', '-')}.txt"
        save_file(output_file, snapshot)

        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "label": label,
            "source": source_path,
            "description": description,
            "output": output_file
        }

        self.reports.append(report)
        self.save_snapshot_reports()
        log_event("Retro Snapshot Recovered", report)
        return report

    def save_snapshot_reports(self):
        with open(RETRO_MEMORY_FILE, "w") as f:
            json.dump(self.reports[-300:], f, indent=2)

    # === Historical Event Simulation System ===

    def load_event_logs(self, path=RETRO_EVENT_LOG_DIR):
        print("📜 Loading retro logs...")
        for filename in os.listdir(path):
            if not filename.endswith(".json"):
                continue
            full_path = os.path.join(path, filename)
            with open(full_path, "r") as f:
                try:
                    data = json.load(f)
                    self.timeline.extend(data if isinstance(data, list) else [data])
                except json.JSONDecodeError:
                    log_event("Corrupt retro log", {"file": filename})

        self.timeline.sort(key=lambda x: x.get("timestamp", ""))

    def reconstruct_history(self):
        print("🧩 Reconstructing historical event chain...")
        replay = []

        for event in self.timeline:
            snippet = {
                "time": event.get("timestamp", "unknown"),
                "description": event.get("summary") or event.get("action") or "Unknown Event",
                "source": event.get("file") or event.get("module")
            }
            replay.append(snippet)

        save_file(RETRO_EVENT_REPLAY_OUTPUT, json.dumps(replay, indent=2))
        log_event("Retro Simulation Built", {"events": len(replay)})
        return replay

# === TEST HARNESS ===
if __name__ == "__main__":
    retro = RetroEngine()

    # Part 1 – Event Log Reconstruction
    retro.load_event_logs()
    timeline = retro.reconstruct_history()
    print(f"📽️ Simulation complete. Reconstructed events: {len(timeline)}")

    # Part 2 – Snapshot Recovery Test
    snapshot = retro.reconstruct_event(
        label="ghostforge_core_restore",
        description="Recovered backup of GhostForge Core",
        source_path="backups/ghostforge_core_bak.py"
    )
    print(json.dumps(snapshot, indent=2))