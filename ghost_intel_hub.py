# === FILE: ghost_intel_hub.py ===
# 🕶️ Ghost Intel Hub – Feeds Malik intel for persona reports

import json
import time
from datetime import datetime
from ghost_queries import get_latest_news, get_market_summary
from file_auto_committer import auto_commit_file

INTEL_FILE = "intel/ghost_feed.json"
LOG_FILE = "logs/ghost_intel.log"

def generate_ghost_intel():
    try:
        print("[GHOST INTEL] 🔍 Fetching fresh intel...")
        news = get_latest_news()
        market = get_market_summary()

        ghost_report = {
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
            "news": news,
            "market_summary": market
        }

        save_ghost_intel(ghost_report)
        auto_commit_file(INTEL_FILE)
        return {"status": "ok", "report": ghost_report}

    except Exception as e:
        print(f"[GHOST INTEL ERROR] ❌ {e}")
        return {"status": "error", "message": str(e)}

def save_ghost_intel(report):
    try:
        with open(INTEL_FILE, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)

        with open(LOG_FILE, "a", encoding="utf-8") as log:
            log.write(f"\n[{report['timestamp']}]\n")
            json.dump(report, log)
            log.write("\n")

        print("[GHOST INTEL] ✅ Saved and logged.")
    except Exception as e:
        print(f"[GHOST INTEL SAVE ERROR] ❌ {e}")