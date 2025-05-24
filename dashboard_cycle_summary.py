import os
import json
from datetime import datetime

CYCLE_SUMMARY_FILE = "data/cycle_summary.json"

def update_cycle_summary(phase, tasks_run, next_cycle_in_sec):
    summary_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "phase": phase,
        "tasks_run": tasks_run,
        "next_cycle_in_sec": next_cycle_in_sec
    }

    with open(CYCLE_SUMMARY_FILE, "w") as f:
        json.dump(summary_data, f, indent=2)

    print(f"[Cycle Summary] Updated summary: {summary_data}")