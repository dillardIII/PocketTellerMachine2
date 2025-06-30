# === botnet_sync.py ===
"""
Botnet Sync – Connects and synchronizes commands, memory, and updates across PTM AI units.
Each node maintains real-time awareness of its neighbors and participates in swarm behavior.
"""

import os
import json
from datetime import datetime
from utils.logger import log_event
from node_mesh import NodeMesh

SYNC_LOG = "memory/botnet_sync_log.json"
COMMAND_QUEUE = "memory/command_queue.json"

class BotnetSync:
    def __init__(self):
        self.mesh = NodeMesh()
        self.sync_log = self.load_log()
        self.command_queue = self.load_commands()

    def load_log(self):
        if not os.path.exists(SYNC_LOG):
            return []
        with open(SYNC_LOG, "r") as f:
            return json.load(f)

    def save_log(self):
        with open(SYNC_LOG, "w") as f:
            json.dump(self.sync_log[-500:], f, indent=2)

    def load_commands(self):
        if not os.path.exists(COMMAND_QUEUE):
            return []
        with open(COMMAND_QUEUE, "r") as f:
            return json.load(f)

    def save_commands(self):
        with open(COMMAND_QUEUE, "w") as f:
            json.dump(self.command_queue[-1000:], f, indent=2)

    def broadcast_command(self, command, origin="PTM"):
        timestamp = datetime.utcnow().isoformat()
        for node_id in self.mesh.list_nodes().keys():
            self.command_queue.append({
                "node": node_id,
                "command": command,
                "origin": origin,
                "timestamp": timestamp
            })

        self.sync_log.append({
            "event": "broadcast",
            "command": command,
            "nodes": list(self.mesh.list_nodes().keys()),
            "timestamp": timestamp
        })

        self.save_log()
        self.save_commands()
        log_event("Botnet Command Broadcast", {
            "command": command,
            "nodes": len(self.mesh.list_nodes())
        })

    def get_pending_commands(self, node_id):
        return [cmd for cmd in self.command_queue if cmd["node"] == node_id]

    def clear_commands(self, node_id):
        self.command_queue = [cmd for cmd in self.command_queue if cmd["node"] != node_id]
        self.save_commands()

if __name__ == "__main__":
    net = BotnetSync()
    net.broadcast_command("SELF_TEST_ALL")
    print("📡 Botnet broadcast sent: SELF_TEST_ALL")