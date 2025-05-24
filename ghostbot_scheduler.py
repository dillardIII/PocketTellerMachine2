import schedule
import time
from ghostbot_brain import ghostbot_think_and_trade

# === Set Up Recurring GhostBot Task ===
def run_ghostbot_loop():
    print("[Scheduler] Running GhostBot Autonomous Cycle...")
    ghostbot_think_and_trade()  # Default ticker is AAPL

# Schedule it to run every 15 minutes
schedule.every(15).minutes.do(run_ghostbot_loop)

print("[Scheduler] GhostBot scheduler is live. Waiting for next cycle...")

# === Keep Scheduler Running ===
while True:
    schedule.run_pending()
    time.sleep(1)