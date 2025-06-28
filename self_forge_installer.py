# === FILE: self_forge_installer.py ===
# 👷 SelfForge Installer – Ensures all core PTM files exist by writing them using GPT

import os
import time
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
CORE_FILES = {
    "auto_strategy_scheduler.py": "Write a Python file that schedules trading strategy prompts every 15 seconds and saves them as .txt files in a ptm_strategy_prompts folder.",
    "auto_code_dropper.py": "Write a Python file that reads .txt prompts from ptm_strategy_prompts, sends them to GPT to generate .py code files, and drops them into ptm_bridge_drop.",
    "meta_dispatcher.py": "Write a Python file that monitors ptm_dashboard.json and prints guidance on whether to use aggressive or conservative strategies based on confidence levels.",
    "ghostforge_core.py": "Write a Python file that mutates trading strategy prompts based on confidence in ptm_dashboard.json and writes new prompts every 30s to ptm_strategy_prompts.",
    "vault_sync_manager.py": "Write a Python file that reads ptm_vault.json and updates ptm_dashboard.json with vault state every 15s."
}

def gpt_write_file(filename, prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You write complete standalone Python .py files only."},
            {"role": "user", "content": prompt}
        ]
    )
    code = response.choices[0].message.content
    with open(filename, "w") as f:
        f.write(code)
    print(f"[SelfForge] 🔥 Created {filename} from scratch.")

def self_forge_loop():
    while True:
        for filename, prompt in CORE_FILES.items():
            if not os.path.exists(filename):
                print(f"[SelfForge] 🚨 {filename} missing — invoking GPT to rebuild.")
                gpt_write_file(filename, prompt)
        time.sleep(60)  # Every minute, check and restore
if __name__ == "__main__":
    self_forge_loop()