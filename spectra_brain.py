#=== FILE: spectra_brain.py ===

""" SpectraBrain – Autonomous Strategic Intelligence for PTM Spectra reads system data, logs, commands, and forecasts to:

Create new modules

Fix broken logic

Make predictive decisions

Drop files into PTM autonomously """


import os import json import time from datetime import datetime from utils.logger import log_event from ghostforge_core import GhostForge from utils.file_utils import save_file

BRIDGE_OUTBOX = "bridge/outbox" SPECTRA_LOG = "logs/spectra_activity.json" os.makedirs(BRIDGE_OUTBOX, exist_ok=True)

class SpectraBrain: def init(self): self.forge = GhostForge(persona="Spectra") self.thought_log = [] self.load_log()

def load_log(self):
    if os.path.exists(SPECTRA_LOG):
        try:
            with open(SPECTRA_LOG, "r") as f:
                self.thought_log = json.load(f)
        except json.JSONDecodeError:
            self.thought_log = []

def save_log(self):
    with open(SPECTRA_LOG, "w") as f:
        json.dump(self.thought_log[-300:], f, indent=2)

def think_and_act(self):
    """
    Core autonomous thought loop – generate & drop modules based on patterns or triggers.
    """
    while True:
        directive = self.analyze_system_state()
        if directive:
            result = self.autogenerate_and_deploy(directive)
            log_event("Spectra Decision", result)
        time.sleep(15)

def analyze_system_state(self):
    # Placeholder logic – can be AI-powered
    now = datetime.utcnow().second
    if now % 2 == 0:
        return "Resync bridge monitors"
    elif now % 5 == 0:
        return "Generate diagnostics report"
    return None

def autogenerate_and_deploy(self, idea):
    module_name = idea.lower().replace(" ", "_")[:40]
    code = f"# Spectra generated: {idea}\nprint('Running: {idea}')"
    generated = self.forge.generate_module(module_name, idea, code, trigger_source="Spectra")
    filename = f"spectra_{module_name}_{datetime.utcnow().isoformat().replace(':', '-')}.py"
    full_path = os.path.join(BRIDGE_OUTBOX, filename)
    save_file(full_path, generated)
    decision = {
        "timestamp": datetime.utcnow().isoformat(),
        "idea": idea,
        "file": filename,
        "status": "deployed"
    }
    self.thought_log.append(decision)
    self.save_log()
    return decision

