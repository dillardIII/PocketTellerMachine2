from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Temporal Sync Engine
Adds time-based awareness, event threading, and predictive continuity to PTM.
Establishes memory anchoring points and syncs state across past-present-future iterations.
Handles time anchors for triggering delayed logic, reminders, and reflex scheduling.
Works with temporal_reflex_daemon to create a cause-effect loop tied to time.
"""

import json
import os
from datetime import datetime, timedelta

# === Legacy + Core Anchors ===
ANCHOR_FILE = "memory/time_anchors.json"
HISTORY_FILE = "memory/event_timeline_log.json"

# === Reflex-Aware Anchors ===
ANCHOR_PATH = "memory/temporal_anchors.json"
LOG_PATH = "memory/temporal_events.json"

# === Timeline Logging ===
def log_event(event: str):
    now = datetime.utcnow().isoformat()
    entry = {"event": event, "timestamp": now}

    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)

    history.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history[-500:], f, indent=2)

    print(f"[TimeSync] Logged event: {event}")

# === Time Anchors (Minutes Offset) ===
def set_anchor(label: str, offset_minutes=0):
    anchors = {}
    if os.path.exists(ANCHOR_FILE):
        with open(ANCHOR_FILE, "r") as f:
            anchors = json.load(f)

    anchor_time = (datetime.utcnow() + timedelta(minutes=offset_minutes)).isoformat()
    anchors[label] = anchor_time

    with open(ANCHOR_FILE, "w") as f:
        json.dump(anchors, f, indent=2)

    print(f"[TimeSync] ⏳ Set anchor '{label}' at {anchor_time}")

def get_anchor(label: str):
    if not os.path.exists(ANCHOR_FILE):
        return None
    with open(ANCHOR_FILE, "r") as f:
        anchors = json.load(f)
    return anchors.get(label)

def has_time_passed(label: str):
    anchor = get_anchor(label)
    if not anchor:
        return False
    return datetime.utcnow() > datetime.fromisoformat(anchor)

# === Reflex Anchor Logic (Seconds Offset) ===
def _load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)

def _save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def set_reflex_anchor(label, delay_seconds):
    anchors = _load_json(ANCHOR_PATH)
    new_time = (datetime.utcnow() + timedelta(seconds=delay_seconds)).isoformat()
    anchors[label] = new_time
    _save_json(ANCHOR_PATH, anchors)
    log_reflex_event(f"Anchor set for '{label}' → {new_time}")

def get_reflex_anchor(label):
    anchors = _load_json(ANCHOR_PATH)
    return anchors.get(label, None)

def has_reflex_time_passed(label):
    anchors = _load_json(ANCHOR_PATH)
    if label not in anchors:
        return False
    now = datetime.utcnow()
    try:
        anchor_time = datetime.fromisoformat(anchors[label])
        return now > anchor_time
    except:
        return False

def log_reflex_event(message):
    events = []
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as f:
            events = json.load(f)

    events.append({
        "timestamp": datetime.utcnow().isoformat(),
        "message": message
    })

    with open(LOG_PATH, "w") as f:
        json.dump(events[-300:], f, indent=2)

# === Wipe Everything (Manual Reset) ===
def reset_time_system():
    for f in [ANCHOR_FILE, HISTORY_FILE, ANCHOR_PATH, LOG_PATH]:
        if os.path.exists(f):
            os.remove(f)
    print("[TimeSync] 🧽 All anchors and logs wiped clean.")

# === CLI Test Trigger ===
if __name__ == "__main__":
    set_anchor("tier_12_entry", offset_minutes=1)
    log_event("Tier 12 temporal sync initialized")
    set_reflex_anchor("reflex_trigger_12", delay_seconds=30)
    log_reflex_event("Reflex anchor set for tier 12.")