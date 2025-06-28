# === FILE: autostart_launcher.py ===

# 🚀 AutoStart Launcher – Boots all PTM systems: bots, reflex, filegen, autowriter

import threading
import time
from start_gpt_bots import start_all_gpt_bots
from reflex_macro_trigger import ReflexMacroTrigger
from strategy_pack_handler import StrategyPackHandler
from reflex_commander import ReflexCommander
from gpt_file_generator_trigger import GPTFileGenTrigger
from auto_code_dropper import AutoCodeDropper
from ghostforge_writer import GhostForgeWriter

# === SYSTEM START ===

trigger = start_all_gpt_bots()
reflex_trigger = ReflexMacroTrigger()
pack_handler = StrategyPackHandler()
reflex_commander = ReflexCommander()
filegen_trigger = GPTFileGenTrigger()
ghost_writer = GhostForgeWriter()
auto_dropper = AutoCodeDropper()

# === BOOT MACROS (OPTIONAL) ===

AUTO_MACROS = [
    "macro: recon launch",
    "macro: sniper sweep"
]

print("[AutoStart] 🚀 Running boot macros...")
for cmd in AUTO_MACROS:
    time.sleep(1)
    if cmd.lower().startswith("macro:"):
        reflex_trigger.process(cmd)
    elif cmd.lower().startswith("drop pack:"):
        pack_handler.drop_pack(cmd.split("drop pack:")[1].strip())
    else:
        trigger.handle_command(cmd)

# === Start Background Services ===

print("[AutoStart] 🧠 Launching ReflexCommander...")
threading.Thread(target=reflex_commander.run_thinking_loop, daemon=True).start()

print("[AutoStart] 🧠 Starting AutoCodeDropper...")
threading.Thread(target=auto_dropper.start, daemon=True).start()

# === MAIN INPUT LOOP ===

print("[AutoStart] 🧠 GPT bot control loop now live.")
while True:
    try:
        cmd = input(">>> Enter command: ").strip()
        if not cmd:
            continue
        if cmd.lower().startswith("drop pack:"):
            pack_handler.drop_pack(cmd.split("drop pack:")[1].strip())
        elif cmd.lower().startswith("macro:"):
            reflex_trigger.process(cmd)
        elif cmd.lower().startswith("generate file:"):
            filegen_trigger.handle_command(cmd)
        elif cmd.lower().startswith("ghostforge build:"):
            try:
                parts = cmd.split("ghostforge build:")[1].split(" with logic:")
                filename = parts[0].strip()
                logic = parts[1].strip()
                ghost_writer.build_and_queue(filename, logic)
            except:
                print("[AutoStart] ❌ Could not parse GhostForge command.")
        else:
            trigger.handle_command(cmd)
    except KeyboardInterrupt:
        print("\n[AutoStart] ⛔ Exiting PTM bots.")
        break