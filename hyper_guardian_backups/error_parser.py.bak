# === FILE: error_parser.py ===
# 🔍 Error Parser – Extracts latest traceback from log files for the self-rebuilder to act on.

import os

ERROR_LOG = "logs/error.log"

def get_latest_error():
    if not os.path.exists(ERROR_LOG):
        return None

    with open(ERROR_LOG, "r") as f:
        lines = f.readlines()

    traceback_lines = []
    in_traceback = False
    file_path = None

    for line in reversed(lines):
        if "Traceback" in line:
            in_traceback = True
            traceback_lines.insert(0, line)
        elif in_traceback:
            traceback_lines.insert(0, line)
            if ".py" in line and "File" in line:
                file_path = line.split('"')[1]
        if in_traceback and line.strip() == "":
            break

    if not traceback_lines:
        return None

    return {
        "file": file_path or "unknown",
        "traceback": "".join(traceback_lines)
    }