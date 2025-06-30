from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: node_register.py ===
# 📌 Node Register – Registers this instance into the GhostNet sync file

import platform
import socket
from datetime import datetime

def register_node(ghostnet):
    node_info = {
        "id": socket.gethostname(),
        "system": platform.system(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "timestamp": str(datetime.now()),
        "status": "online"
    }
    ghostnet.add_node(node_info)
    print(f"[Node] 🧬 Registered node: {node_info['id']}")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():