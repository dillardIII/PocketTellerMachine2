from ghost_env import INFURA_KEY, VAULT_ADDRESS
# recovery_daemon.py

import time
from bot_tracker import get_bot_status, restart_bot
from logger import log_event

RECOVERY_INTERVAL = 10  # seconds

def recovery_loop():
    """
    Continuously monitors bots and restarts those that have crashed or frozen.
    """
    print("[RECOVERY] Recovery daemon online.")
    while True:
        try:
            bot_statuses = get_bot_status()
            for bot in bot_statuses:
                name = bot["name"]
                if bot["status"] in ["crashed", "unresponsive"]:
                    print(f"[RECOVERY] Bot '{name}' is {bot['status']}. Initiating restart.")
                    restart_bot(name)
                    log_event("recovery", f"Restarted bot '{name}' due to status '{bot['status']}'")
        except Exception as e:
            log_event("recovery_error", str(e))
        time.sleep(RECOVERY_INTERVAL)

if __name__ == "__main__":
    recovery_loop()