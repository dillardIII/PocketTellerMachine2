# === FILE: file_exec_router.py ===

# 📦 File Exec Router – Routes file types to proper handlers (optional, extendable)

def route_file_execution(filename):
    if filename.endswith(".py"):
        return "python"
    elif filename.endswith(".json"):
        return "json_handler"
    else:
        return "unsupported"