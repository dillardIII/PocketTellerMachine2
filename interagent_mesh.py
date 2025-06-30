from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
InterAgent Mesh Network
Enables all AI personas to communicate, challenge, and collaborate on internal decisions.
Simulates collective reasoning and autonomous debates.
"""

import json
import os
import random
from datetime import datetime

MESH_LOG = "memory/mesh_conversations.json"
PERSONAS = ["Mentor", "Mo Cash", "Strategist", "Drill Instructor", "Shadow", "Optimist", "Chill Trader", "GhostBot"]

def load_mesh_log():
    if not os.path.exists(MESH_LOG):
        return []
    with open(MESH_LOG, "r") as f:
        return json.load(f)

def save_mesh_log(log):
    with open(MESH_LOG, "w") as f:
        json.dump(log[-300:], f, indent=2)

def generate_response(from_agent, to_agent, topic):
    verbs = ["agrees with", "disagrees with", "modifies", "reinforces", "questions", "expands on"]
    verb = random.choice(verbs)
    return f"{from_agent} {verb} {to_agent}'s idea on '{topic}'"

def simulate_conversation(topic: str, turns: int = 4):
    log = load_mesh_log()
    agents = random.sample(PERSONAS, k=min(4, len(PERSONAS)))
    
    for i in range(turns):
        a1, a2 = random.sample(agents, 2)
        line = {
            "timestamp": datetime.utcnow().isoformat(),
            "speaker": a1,
            "response": generate_response(a1, a2, topic),
            "topic": topic
        }
        log.append(line)
        print(f"[MeshNet] {line['speaker']}: {line['response']}")

    save_mesh_log(log)

# Example
if __name__ == "__main__":
    simulate_conversation("risk tolerance in volatile markets")

def log_event():ef drop_files_to_bridge():