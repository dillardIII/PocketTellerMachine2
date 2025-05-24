import os
import json
import traceback

ERROR_LOG_FILE = "logs/error_log.txt"

# === Save an Error Manually (Optional) ===
def save_error_to_log(exc_info):
    os.makedirs("logs", exist_ok=True)
    with open(ERROR_LOG_FILE, "a") as f:
        f.write("".join(traceback.format_exception(*exc_info)) + "\n\n")

# === Extract Most Recent Error ===
def get_latest_error():
    if not os.path.exists(ERROR_LOG_FILE):
        return None

    with open(ERROR_LOG_FILE, "r") as f:
        lines = f.readlines()

    latest = []
    for line in reversed(lines):
        if line.strip() == "":
            if latest:
                break
        latest.insert(0, line)

    error_text = "".join(latest).strip()
    if "File" in error_text:
        for line in latest:
            if "File" in line and ".py" in line:
                parts = line.strip().split(", ")
                file_path = parts[0].split('"')[1]
                line_num = parts[1].split(" ")[1]
                return {
                    "file": file_path,
                    "line": int(line_num),
                    "error": error_text
                }

    return {"file": "unknown", "line": 0, "error": error_text}