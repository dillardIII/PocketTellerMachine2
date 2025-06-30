from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: start_gpt_bots.py ===

# 🧠 GPT Bot Startup – Now with full macro + reflex command logic

import threading
from gpt_trigger_handler import GPTTriggerHandler
from gpt_file_drop_agent import GPTFileDropAgent
from file_map import file_map
from strategy_pack_handler import StrategyPackHandler
from reflex_macro_trigger import ReflexMacroTrigger

trigger = GPTTriggerHandler(file_map)
drop_agent = GPTFileDropAgent()
pack_handler = StrategyPackHandler()
reflex_trigger = ReflexMacroTrigger()

def start_all_gpt_bots():
    print("[GPT Bots] 🔄 Starting GPT-side automation bots...")
    threading.Thread(target=drop_agent.start, daemon=True).start()
    return trigger

# 🧠 GPT Command Loop (AUTONOMOUS MODE)
if __name__ == "__main__":
    trigger = start_all_gpt_bots()
    while True:
        cmd = input(">>> Enter command: ").strip()
        if not cmd:
            continue
        if cmd.lower().startswith("drop pack:"):
            pack_name = cmd.split("drop pack:")[1].strip()
            pack_handler.drop_pack(pack_name)
        elif cmd.lower().startswith("macro:"):
            reflex_trigger.process(cmd)
        else:
            trigger.handle_command(cmd)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():