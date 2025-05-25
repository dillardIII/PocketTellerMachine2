# === FILE: error_parser.py ===

import os
import json
import traceback
from datetime import datetime

# === Log Paths ===
JSON_ERROR_LOG_FILE = "logs/error_log.json"
TXT_ERROR_LOG_FILE = "logs/error_log.txt"

# === Save Error to Both Logs ===
def save_error_to_log(exc_info):
    os.makedirs("logs", exist_ok=True)

    error_type, error_value, tb = exc_info
    tb_str = "".join(traceback.format_exception(error_type, error_value, tb))
    filename = extract_file_from_traceback(tb)

    error_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "file": filename,
        "error_message": str(error_value),
        "traceback": tb_str
    }

    # === Save to JSON log ===
    try:
        if os.path.exists(JSON_ERROR_LOG_FILE):
            with open(JSON_ERROR_LOG_FILE, "r") as f:
                data = json.load(f)
        else:
            data = []

        data.append(error_entry)

        with open(JSON_ERROR_LOG_FILE, "w") as f:
            json.dump(data, f, indent=2)

        print(f"[Error Parser] Error logged in JSON from file: {filename}")
    except Exception as e:
        print(f"[Error Parser] Failed to save JSON error log: {e}")

    # === Save to plain text log (optional for review/debug) ===
    try:
        with open(TXT_ERROR_LOG_FILE, "a") as f:
            f.write(tb_str + "\n\n")
    except Exception as e:
        print(f"[Error Parser] Failed to save TXT error log: {e}")

# === Extract File from Traceback Object ===
def extract_file_from_traceback(tb):
    while tb.tb_next:
        tb = tb.tb_next
    return tb.tb_frame.f_code.co_filename

# === Get Most Recent Error ===
def get_latest_error():
    if os.path.exists(JSON_ERROR_LOG_FILE):
        try:
            with open(JSON_ERROR_LOG_FILE, "r") as f:
                data = json.load(f)
                if data:
                    latest = data[-1]
                    return {
                        "file": latest.get("file"),
                        "error_message": latest.get("error_message"),
                        "traceback": latest.get("traceback")
                    }
        except Exception as e:
            print(f"[Error Parser] Failed to read JSON log: {e}")

    elif os.path.exists(TXT_ERROR_LOG_FILE):
        try:
            with open(TXT_ERROR_LOG_FILE, "r") as f:
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
        except Exception as e:
            print(f"[Error Parser] Failed to read TXT log: {e}")

    return None
