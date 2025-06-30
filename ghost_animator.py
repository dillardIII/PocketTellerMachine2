# === FILE: GhostAnimator.py ===
# 👻 GHOST ANIMATOR
# Console glitch animation for ghost mood.

import time
import random

def glitch_line():
    chars = ["▓","▒","░","█","▄","▀","█","▓"]
    line = "".join(random.choice(chars) for _ in range(60))
    print(line)

def main():
    print("[GhostAnimator] 👻 Starting ghost glitch show...")
    for _ in range(10):
        glitch_line()
        time.sleep(0.2)

if __name__ == "__main__":
    main()