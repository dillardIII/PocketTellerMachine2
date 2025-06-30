# === FILE: gpt_self_command_engine.py ===
# Self-directed command generation system for GPT inside PTM

import random
import json
import os
from datetime import datetime

from ptm_gpt_agent import run_ptm_gpt_agent
from cole_gpt_advisor import ask_gpt
from cole_brain import get_current_focus
from strategy_module_loader import get_strategy_modules
from gpt_prompt_engine import generate_prompt
from gpt_executor import execute_command

LOG_FILE = "logs/self_commands_log.json"
PROMPT_HISTORY = []

def generate_self_command():
    """
    Primary method for autonomous GPT command generation based on focus + strategy modules.
    """
    print("[Self Command] 🔄 Starting dual-generation routine...")

    # === ROUND 1: From Cole's focus and strategy
    try:
        focus = get_current_focus()
        print(f"[Self Command] 🎯 Current Focus: {focus}")

        strategies = get_strategy_modules()
        print(f"[Self Command] 📚 Strategies Available: {len(strategies)}")

        if strategies:
            selected = random.choice(strategies)
            print(f"[Self Command] 🧠 Strategy Selected: {selected.name}")

            prompt = generate_prompt(selected, focus)
            print(f"[Self Command] 💬 Prompt Generated")

            result = execute_command(prompt)
            log_command(prompt, result)
            print(f"[Self Command] ✅ Strategy Command Executed: {result}")
        else:
            print("[Self Command] ⚠️ No strategies found")

    except Exception as e:
        print(f"[Self Command] ⚠️ Error in strategy generation: {e}")

    # === ROUND 2: GPT-guided prompt generation
    try:
        base_prompt = """
You are the self-command brain for PTM.

Your job is to create a useful improvement prompt that will help PTM evolve, learn, or gain a new skill.

Only generate commands that make sense for an AI trading assistant and system builder. Avoid redundancy.

Example format:
"Add a trading dashboard to compare crypto vs stocks."

Now create one new command PTM can work on.
"""
        response = ask_gpt(base_prompt).strip()

        if response:
            PROMPT_HISTORY.append(response)
            print(f"[GPT Command Engine] Submitting: {response}")
            result = run_ptm_gpt_agent(response)
            log_command(response, result)
            print(f"[GPT Command Engine] ✅ GPT Agent Executed: {result}")
        else:
            print("[GPT Command Engine] Empty response. Skipping.")

    except Exception as e:
        print(f"[GPT Command Engine] ⚠️ GPT Error: {e}")

def log_command(prompt, result):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "result": result
    }

    os.makedirs("logs", exist_ok=True)

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(log_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs[-200:], f, indent=2)