# === FILE: enhanced_gpt_swarm.py ===
import os, time, random
from datetime import datetime
from openai import OpenAI

BRIDGE_DIR = "ptm_bridge_drop"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
counter = 0

PROMPT_TEMPLATES = [
    "Create a new self-healing Python module for PTM empire that optimizes trading after losses.",
    "Invent a reinforcement learning trading script for the PTM empire.",
    "Write a ghost-data processor that remembers market patterns.",
    "Design a volatility strategy script with autonomous memory updates.",
    "Create a new GPT-driven module that reads logs and suggests improvements."
]

def generate_file():
    global counter
    prompt = random.choice(PROMPT_TEMPLATES)
    print(f"[GPTSwarm] 🧠 Prompt: {prompt}")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    code = response.choices[0].message.content
    filename = f"swarm_module_{counter}.py"
    path = os.path.join(BRIDGE_DIR, filename)
    with open(path, "w") as f:
        f.write(code)
    print(f"[GPTSwarm] ✍️ Dropped: {path}")
    counter += 1

def swarm_loop():
    print("[GPTSwarm] 🐙 Autonomous GPT swarm running...")
    while True:
        generate_file()
        time.sleep(random.randint(60, 120))  # vary intervals to look more organic

if __name__ == "__main__":
    swarm_loop()