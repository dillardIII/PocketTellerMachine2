import json
import os

LOG_FILE = "data/cole_brain_log.json"

def sanitize_log_file():
    try:
        with open(LOG_FILE, "r") as f:
            content = f.read()

        # Fix common issues
        content = content.strip()

        # Ensure proper commas between entries if user pasted broken logs
        content = content.replace("}\n{", "},\n{")

        # Ensure it's wrapped in a list if not already
        if not content.startswith("["):
            content = "[" + content
        if not content.endswith("]"):
            content = content + "]"

        # Try parsing
        data = json.loads(content)

        with open(LOG_FILE, "w") as f:
            json.dump(data, f, indent=2)

        print("[Log Sanitizer] Log file sanitized successfully.")

    except Exception as e:
        print(f"[Log Sanitizer] Failed to sanitize log: {e}")