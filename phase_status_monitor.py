# phase_status_monitor.py
# Monitors PTM startup phases and flags issues for debugging

import time

phase_status = {
    "boot": False,
    "autonomy": False,
    "bots": False,
    "ui": False
}

def set_phase_status(phase, status=True):
    if phase in phase_status:
        phase_status[phase] = status
        print(f"[PhaseStatus] ✅ {phase} phase set to {status}")
    else:
        print(f"[PhaseStatus] ⚠️ Unknown phase '{phase}'")

def monitor():
    print("[PhaseStatus] 🛰️ Monitoring system phase progress...")
    while True:
        print(f"[PhaseStatus] 📊 Status: {phase_status}")
        time.sleep(15)