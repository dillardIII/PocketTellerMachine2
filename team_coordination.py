from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: team_coordinator.py ===
import os, json

def check_other_bots(team_dir="team_memory"):
    if not os.path.exists(team_dir):
        os.makedirs(team_dir)
    states = []
    for file in os.listdir(team_dir):
        if file.endswith(".json"):
            with open(os.path.join(team_dir, file)) as f:
                states.append(json.load(f))
    return states

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():