from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: matrix_dashboard.py ===
# 🟢 PTM Matrix Console Dashboard – shows modules, nodes, vault activity in cyber style

import os
import time
import json
import random
from datetime import datetime

def get_active_modules():
    # This could be enhanced to actually scan psutil or a file record of processes
    modules = [
        "main.py", "quantum_auto_scaler.py", "idle_mutator.py",
        "ghost_autogenesis.py", "module_auto_launcher.py",
        "multi_vps_replication.py", "self_rebuilder.py",
        "tamper_guard.py", "universal_file_integrator.py",
        "dynamic_module_loader.py", "bridge_exec_orchestrator.py",
        "dropbull_pulse.py", "context_ai.py", "global_voice_feed.py"
    ]
    active = random.sample(modules, k=random.randint(5, len(modules)))
    return active

def get_node_health():
    try:
        with open("node_map.json") as f:
            return json.load(f)
    except:
        return []

def get_brain_status():
    try:
        with open("brain_status.json") as f:
            return json.load(f)
    except:
        return {"total_brains": 0, "queue": 0, "mood": "unknown"}

def get_vault_logs():
    try:
        with open("vault/vault_log.json") as f:
            logs = json.load(f)
            return logs[-5:]  # show last 5 events
    except:
        return []

def render_dashboard():
    os.system('clear' if os.name == 'posix' else 'cls'):
    print("=" * 80)
    print("🧬 PTM MATRIX CONSOLE DASHBOARD".center(80))
    print("=" * 80)

    # Active Modules
    print("\n🛠️ ACTIVE EMPIRE MODULES:")
    for m in get_active_modules():
        print(f"  ▶️ {m}")

    # Node Health
    print("\n🌐 NODE MAP:")
    nodes = get_node_health()
    for node in nodes:
        print(f"  • {node['id']} | Status: {node['status']} | Last Ping: {node['last_ping']}")

    # Brain Status
    bs = get_brain_status()
    print(f"\n⚛️ QUANTUM BRAINS: {bs.get('total_brains')} | Queue: {bs.get('queue')} | Mood: {bs.get('mood')}")

    # Vault Activity
    print("\n💼 RECENT VAULT EVENTS:")
    for e in get_vault_logs():
        print(f"  [{e['timestamp']}] {e['type']} -> {str(e['data'])[:50]}")

    print("\n" + "=" * 80)
    print(f"Updated at: {datetime.utcnow().isoformat()}")
    print("=" * 80)

if __name__ == "__main__":
    while True:
        render_dashboard()
        time.sleep(10)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():