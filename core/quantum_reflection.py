from ghost_env import INFURA_KEY, VAULT_ADDRESS
# quantum_reflection.py
# Reviews what the mind is thinking and evolves it

import json

def reflect_on_mind():
    try:
        with open("memory/ghostmind_log.json", "r") as f:
            logs = json.load(f)
    except:
        logs = []

    reflections = []
    for entry in logs[-10:]:
        if "trade" in str(entry["thought"]).lower():
            reflections.append(f"Reflection: Strategy triggered by {entry['thought']}")
        elif "error" in str(entry["thought"]).lower():
            reflections.append(f"Alert: Mind noticed flaw - {entry['thought']}")

    return reflections