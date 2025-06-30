from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === node_mesh.py ===
"""
Node Mesh – Multinode Awareness System
Tracks PTM-connected nodes across devices, locations, and bridges.
Supports routing, ping tests, and collaborative AI mesh behavior.
"""

import os
import json
from datetime import datetime
from utils.logger import log_event

NODE_CONFIG = "memory/nodes.json"
NODE_LOG = "memory/node_mesh_log.json"

class NodeMesh:
    def __init__(self, persona="MeshAI"):
        self.persona = persona
        self.nodes = self.load_nodes()
        self.history = self.load_log()

    def load_nodes(self):
        if not os.path.exists(NODE_CONFIG):
            return {}
        with open(NODE_CONFIG, "r") as f:
            return json.load(f)

    def load_log(self):
        if not os.path.exists(NODE_LOG):
            return []
        with open(NODE_LOG, "r") as f:
            return json.load(f)

    def save_log(self):
        with open(NODE_LOG, "w") as f:
            json.dump(self.history[-300:], f, indent=2)

    def register_node(self, node_id, meta):
        self.nodes[node_id] = {
            "registered_at": datetime.utcnow().isoformat(),
            "meta": meta,
            "last_ping": datetime.utcnow().isoformat()
        }
        self.save_nodes()
        self.history.append({
            "event": "register",
            "node": node_id,
            "timestamp": datetime.utcnow().isoformat()
        })
        self.save_log()
        log_event("Node Registered", {"node": node_id, "meta": meta})

    def ping_node(self, node_id):
        if node_id in self.nodes:
            self.nodes[node_id]["last_ping"] = datetime.utcnow().isoformat()
            self.save_nodes()
            log_event("Node Pinged", {"node": node_id})
            return True
        return False

    def list_nodes(self):
        return self.nodes

    def save_nodes(self):
        with open(NODE_CONFIG, "w") as f:
            json.dump(self.nodes, f, indent=2)

if __name__ == "__main__":
    mesh = NodeMesh()
    print("🌐 Active Nodes:")
    for nid, details in mesh.list_nodes().items():
        print(f"- {nid} → {details['meta']}")