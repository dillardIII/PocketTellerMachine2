# === FILE: auto_mutator.py ===

# 🧬 AutoMutator – Applies random changes to evolve strategies

import random

def mutate_code(code):
    print("[AutoMutator] 🧬 Mutating code...")
    if "RSI" in code:
        code = code.replace("RSI", "StochRSI")
    if "20" in code:
        code = code.replace("20", str(random.randint(10, 30)))
    return code