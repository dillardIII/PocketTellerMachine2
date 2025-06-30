from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: gpt_outbound/file_creator.py ===
# ✍️ File Creator – GPT bots save files in outbound for drop agent

import os

def save_file(filename, content):
    os.makedirs("gpt_outbound", exist_ok=True)
    filepath = os.path.join("gpt_outbound", filename)

    with open(filepath, "w") as f:
        f.write(content)

    print(f"[File Creator] 📄 Created outbound file: {filename}")