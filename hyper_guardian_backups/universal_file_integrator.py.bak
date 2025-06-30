# 🔗 Integrates any new scripts into empire modules automatically
import os
import shutil
import time

WATCH = "ptm_inbox"
DEST = "ptm_modules"
os.makedirs(WATCH, exist_ok=True)
os.makedirs(DEST, exist_ok=True)

print("[Integrator] 🔗 Watching for new modules...")
while True:
    for f in os.listdir(WATCH):
        src = os.path.join(WATCH, f)
        dest = os.path.join(DEST, f)
        if os.path.isfile(src) and f.endswith(".py"):
            shutil.move(src, dest)
            print(f"[Integrator] ✅ Integrated module: {f}")
    time.sleep(5)