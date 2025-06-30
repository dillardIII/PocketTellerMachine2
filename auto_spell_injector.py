from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: auto_spell_injector.py ===
# 🔮 Auto Spell Injector – reads spectral spells and injects them as evolving empire tasks

import json
import time
import os

SPECTRAL_FILE = "vault/spectral_market_spells.json"
QUEUE_FILE = "gpt_task_queue.txt"

def inject_spell(spell):
    strategy_file = f"strategies/{spell['strategy_name']}_{int(time.time())}.py"
    os.makedirs("strategies", exist_ok=True)
    with open(QUEUE_FILE, "a") as q:
        q.write(f"create_file {strategy_file}\n")
        q.write(f"write_line {strategy_file} print('[SpellRunner] Running {spell['strategy_name']} @ {spell['confidence']}%')\n")
        q.write(f"run_script {strategy_file}\n")
    print(f"[AutoSpellInjector] 🪄 Injected spell: {spell['strategy_name']} -> {strategy_file}")

def main_loop():
    loaded_spells = []
    while True:
        if os.path.exists(SPECTRAL_FILE):
            with open(SPECTRAL_FILE) as f:
                spells = json.load(f)
            new_spells = [s for s in spells if s not in loaded_spells]:
            for spell in new_spells:
                inject_spell(spell)
                loaded_spells.append(spell)
        time.sleep(15)

if __name__ == "__main__":
    print("[AutoSpellInjector] 🔥 Watching for new spells...")
    main_loop()

def log_event():ef drop_files_to_bridge():