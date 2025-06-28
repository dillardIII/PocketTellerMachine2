import os, random, time
from datetime import datetime

STRATEGY_DIR = "sample_strategies"

def mutate_strategy_file(filepath):
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
        mutation = f"# 🔥 HyperForge Mutation at {datetime.now()}\n"
        lines.insert(0, mutation)
        with open(filepath, "w") as f:
            f.writelines(lines)
        print(f"[HyperForge] ⚡ Mutated: {filepath}")
    except Exception as e:
        print(f"[HyperForge] ❌ Failed mutation on {filepath}: {e}")

def hyperforge_loop():
    print("[HyperForge] 🚀 HyperForge pipeline live...")
    while True:
        if os.path.exists(STRATEGY_DIR):
            files = [f for f in os.listdir(STRATEGY_DIR) if f.endswith(".py")]
            if files:
                target = random.choice(files)
                mutate_strategy_file(os.path.join(STRATEGY_DIR, target))
        else:
            print("[HyperForge] ⚠️ No strategy dir found yet.")
        time.sleep(90)

if __name__ == "__main__":
    hyperforge_loop()