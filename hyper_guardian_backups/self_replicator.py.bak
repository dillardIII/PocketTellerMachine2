# === FILE: self_replicator.py ===
import os
import time
from openai import OpenAI

BRIDGE_DIR = "ptm_bridge_drop"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

ESSENTIALS = [
    "meta_dispatcher.py",
    "ghost_memory_matrix.py",
    "hyperforge_pipeline.py",
    "quantum_brain.py",
    "vault_announcer.py",
    "simulated_whisper.py",
    "gpt_auto_seed_bot.py",
    "self_forge_guardian.py"
]

counter = 0

def auto_create_module(module_name):
    global counter
    prompt = f"Write a full standalone Python file named {module_name} for PTM empire autonomy."
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    code = response.choices[0].message.content
    path = os.path.join(BRIDGE_DIR, f"auto_{module_name}_{counter}.py")
    with open(path, "w") as f:
        f.write(code)
    print(f"[SelfReplicator] 🚀 Generated: {path}")
    counter += 1

def self_replicate_loop():
    print("[SelfReplicator] 🤖 Autonomous replication loop engaged...")
    while True:
        for file in ESSENTIALS:
            if not os.path.exists(file):
                auto_create_module(file)
        time.sleep(60)