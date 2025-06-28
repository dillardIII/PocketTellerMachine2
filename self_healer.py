# === FILE: self_healer.py ===
# Attempts automatic repairs when logic or execution errors occur

import traceback

def try_repair(fn, fallback=None):
    try:
        return fn()
    except Exception as e:
        print("[🛠️ SELF-HEALING] Error detected. Attempting repair...")
        traceback.print_exc()
        if fallback:
            try:
                return fallback()
            except Exception as fe:
                print("[🔥 FAILOVER] Fallback also failed.")
                traceback.print_exc()
        return None