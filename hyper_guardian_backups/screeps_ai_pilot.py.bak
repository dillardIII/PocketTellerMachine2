# === FILE: screeps_ai_pilot.py ===
from screepsapi import API

def run_ai_loop():
    api = API(u='your_username', p='your_password')
    memory = api.memory()

    if 'energy' in memory:
        if memory['energy'] < 300:
            print("🔋 Low energy. Building Harvester.")
            api.memory('spawn_task', 'spawn_harvester')
        else:
            print("🔧 Sufficient energy. Expanding Builder network.")
            api.memory('spawn_task', 'spawn_builder')

    # Update PTM logs
    print("✅ Screeps AI loop completed.")