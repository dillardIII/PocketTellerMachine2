from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 🧠 Quantum Signal Manager – Handles deep signal tracking across devices and AI layers

import os
import json
import time
from utils.logger import log_event

SIGNAL_FILE = "data/quantum_signals.json"
ACTIVE_DEVICES = ["Predator", "ZFold6", "S10Ultra"]
SIGNAL_LOG = "logs/quantum_signal_log.json"

def load_signals():
    if os.path.exists(SIGNAL_FILE):
        with open(SIGNAL_FILE, "r") as f:
            return json.load(f)
    return {}

def save_signal(device, signal_data):
    signal_log = {}
    if os.path.exists(SIGNAL_LOG):
        with open(SIGNAL_LOG, "r") as f:
            signal_log = json.load(f)
    if device not in signal_log:
        signal_log[device] = []
    signal_log[device].append(signal_data)
    with open(SIGNAL_LOG, "w") as f:
        json.dump(signal_log, f, indent=2)

def scan_device_signals():
    signals = load_signals()
    for device in ACTIVE_DEVICES:
        signal = signals.get(device, {})
        log_event("QuantumSignal", {"device": device, "signal": signal})
        save_signal(device, {"timestamp": time.time(), "signal": signal})

def signal_loop():
    print("[QuantumSignal] 🛰️ Scanning quantum signal nodes...")
    while True:
        scan_device_signals()
        time.sleep(30)

if __name__ == "__main__":
    signal_loop()