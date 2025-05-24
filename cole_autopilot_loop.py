from flask import Flask, jsonify, request, redirect, url_for
import os, json
from datetime import datetime

# === Cole Imports ===
from cole_auto_system import cole_autopilot_cycle
from error_parser import get_latest_error, save_error_to_log
from ai_code_generator import generate_code_fix
from auto_deployer import deploy_fix

app = Flask(__name__)

# === Background Autopilot Runner with Self-Healing ===
def run_autopilot_safe():
    try:
        cole_autopilot_cycle()
    except Exception as e:
        import sys
        save_error_to_log(sys.exc_info())
        print("[Cole Autopilot] Logged error:", e)

# === Optional: Run on Startup ===
if __name__ == '__main__':
    from threading import Thread
    Thread(target=run_autopilot_safe, daemon=True).start()
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)

# === Manual Trigger for Self-Healing ===
@app.route("/fix_now")
def manual_fix_now():
    error = get_latest_error()
    if not error:
        return jsonify({"status": "no error found"})

    fix = generate_code_fix(error)
    if not fix:
        return jsonify({"status": "fix generation failed"})

    success = deploy_fix(error["file"], fix)
    if success:
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "file": error["file"],
            "error": error["error"],
            "fix": fix
        }
        os.makedirs("data", exist_ok=True)
        fixes_log = "data/fixes_log.json"
        try:
            if os.path.exists(fixes_log):
                with open(fixes_log, "r") as f:
                    data = json.load(f)
            else:
                data = []
            data.append(log_entry)
            with open(fixes_log, "w") as f:
                json.dump(data, f, indent=2)
        except:
            pass
        return jsonify({"status": "fixed", "file": error["file"]})
    else:
        return jsonify({"status": "fix failed", "file": error["file"]})