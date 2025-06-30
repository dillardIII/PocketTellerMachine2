# === FILE: ghost_vault_survey_cyber.py ===
import json
import random
import time

CYBER_FILE = "ghost_cyber_state.json"

def load_cyber_state():
    try:
        with open(CYBER_FILE, "r") as f:
            return json.load(f)
    except:
        return {"aggression":0.5,"stealth":0.5,"greed":0.5,"propaganda_intensity":0.5}

def survey_loop():
    print("[GhostVaultSurvey] 🏦 Vault survey mesh live...")
    while True:
        cyber = load_cyber_state()
        vault_balance = round(random.uniform(5, 20), 4)
        if vault_balance < 7:
            print(f"[GhostVaultSurvey] ⚠️ Low vault: {vault_balance} ETH. Cyber stealth {cyber['stealth']:.2f} ↑ caution.")
        elif vault_balance > 15:
            print(f"[GhostVaultSurvey] 💰 High vault: {vault_balance} ETH. Cyber greed {cyber['greed']:.2f} ↑ expansion.")
        else:
            print(f"[GhostVaultSurvey] 🔄 Stable vault: {vault_balance} ETH.")
        time.sleep(90)

if __name__ == "__main__":
    survey_loop()