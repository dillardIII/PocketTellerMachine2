from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: auto_ui_generator.py ===
# 🧱 Auto UI Generator – Builds UI views from bot data and strategies

import os
import json

TEMPLATE = """
<div class="strategy-card">
    <h3>{name}</h3>
    <p><strong>Type:</strong> {type}</p>
    <p><strong>Status:</strong> {status}</p>
    <p><strong>Assigned To:</strong> {assigned}</p>
</div>
"""

def generate_ui_cards(strategy_file="strategy_registry.json", output="templates/strategy_cards.html"):
    if not os.path.exists(strategy_file):
        print("[AutoUI] ❌ No strategy_registry.json found.")
        return

    with open(strategy_file, "r") as f:
        strategies = json.load(f)

    blocks = []
    for s in strategies:
        html = TEMPLATE.format(
            name=s.get("name", "Unnamed"),
            type=s.get("type", "Unknown"),
            status=s.get("status", "Idle"),
            assigned=s.get("assigned", "None")
        )
        blocks.append(html)

    os.makedirs("templates", exist_ok=True)
    with open(output, "w") as out:
        out.write("\n".join(blocks))

    print(f"[AutoUI] ✅ Generated strategy_cards.html with {len(blocks)} panels.")

if __name__ == "__main__":
    generate_ui_cards()

def log_event():ef drop_files_to_bridge():