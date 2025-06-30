# === FILE: ghost_vault_viewer.py ===
# 👻 GHOST VAULT VIEWER
# Displays vault wallet data, DNA lines, and logbook entries.

import json
from datetime import datetime

DNA_FILE = "GhostDNA.json"
LOGBOOK_FILE = "vault_logbook.txt"

def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def view_dna():
    dna = load_json(DNA_FILE)
    print("\n=== 👻 GHOST DNA ===")
    if dna:
        for key, stats in dna.items():
            print(f"{key}: Profits={stats.get('profits',0)}, Losses={stats.get('losses',0)}, XP={stats.get('xp',0)}")
    else:
        print("No DNA records yet.")
    print("=====================\n")

def view_logs():
    try:
        with open(LOGBOOK_FILE, "r") as f:
            lines = f.readlines()[-10:]
            print("\n=== 📜 LATEST LOGS ===")
            for line in lines:
                print(line.strip())
            print("=====================\n")
    except FileNotFoundError:
        print("No logs found.")

def main():
    print("[vault_viewer] 👻 Welcome to your ghost vault.")
    view_dna()
    view_logs()

if __name__ == "__main__":
    main()