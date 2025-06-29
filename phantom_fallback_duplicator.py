# 💀 Phantom Duplication – If disrupted, spawns elsewhere instantly
import os, time, random, shutil

def duplicate_self():
    target = f"phantom_copy_{int(time.time())}.py"
    shutil.copy(__file__, target)
    print(f"[PhantomDuplicator] 🕷️ Spawned to {target}")

while True:
    duplicate_self()
    time.sleep(random.randint(300,600))