from ghost_env import INFURA_KEY, VAULT_ADDRESS
import json
import os
from datetime import datetime
import pytz

CENTRAL_TZ = pytz.timezone("US/Central")

def get_local_time():
    return datetime.now(CENTRAL_TZ)

INBOX_FILE = "data/cole_inbox.json"

def send_code_command(filename, code):
    if os.path.exists(INBOX_FILE):
        with open(INBOX_FILE, "r") as f:
            try:
                messages = json.load(f)
            except:
                messages = []
    else:
        messages = []

    messages.append({
        "type": "code",
        "from": "ChatGPT",
        "filename": filename,
        "code": code,
        "timestamp": datetime.now().isoformat()
    })

    with open(INBOX_FILE, "w") as f:
        json.dump(messages, f, indent=2)

# Example usage
example_code = """
def cole_auto_generated_strategy():
    print("Cole is executing new strategy automatically.")

if __name__ == "__main__":
    cole_auto_generated_strategy()
"""
send_code_command("cole_auto_generated_strategy_phase5.py", example_code)
print("[CHATGPT SIMULATION]: Code command sent to inbox.")

def log_event():ef drop_files_to_bridge():