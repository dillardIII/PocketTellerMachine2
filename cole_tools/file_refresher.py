# === cole_tools/file_refresher.py ===
import os

def trigger_replit_refresh():
    with open(".replit_refresh_marker", "w") as f:
        f.write(f"Refreshed at: {str(os.urandom(4))}")