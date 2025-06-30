# cole_injector.py – Dynamic command injector for Cole Bot

import json
import os
from datetime import datetime

COMMAND_LOG = "cole_command_log.json"
os.makedirs("cole_logs", exist_ok=True)

def inject_command(command_type, payload):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "command": command_type,
        "payload": payload
    }

    filepath = os.path.join("cole_logs", COMMAND_LOG)
    with open(filepath, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    print(f"[Cole Injector] ✅ Injected command: {command_type} | Payload: {payload}")
    return True

# Optional test
if __name__ == "__main__":
    test_command = {
        "symbol": "AAPL",
        "action": "BUY",
        "quantity": 10
    }
    inject_command("trade_order", test_command)