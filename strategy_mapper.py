from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: strategy_mapper.py ===
# FixOps Commander: Error trend analysis and tactical insight generator

import os
import json
from collections import defaultdict
from datetime import datetime

# File paths
REPAIR_LOG = "logs/repair_log.json"
AUTOFIX_LOG = "logs/autofix_engine_log.json"
INSIGHT_OUTPUT = "logs/strategy_insight.json"
REPO_FILE = "repo_requests.json"

# Thresholds
FAIL_THRESHOLD = 2

def load_log(log_file):
    if os.path.exists(log_file):
        try:
            with open(log_file, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"[Mapper] ⚠️ Malformed JSON in {log_file}")
            return []
    return []

def escalate_to_gpt(module):
    print(f"[StrategyMapper] 🚨 Escalating {module} to GPT repair.")
    try:
        with open(REPO_FILE, "w") as f:
            json.dump({"needs": [module]}, f, indent=2)
    except Exception as e:
        print(f"[StrategyMapper] ❌ Failed to escalate {module}: {e}")

def analyze_trends_and_escalate():
    repair_log = load_log(REPAIR_LOG)
    autofix_log = load_log(AUTOFIX_LOG)

    fail_count = defaultdict(int)
    modules = defaultdict(lambda: {"repairs": 0, "autofixes": 0})

    for entry in repair_log:
        for req in entry.get("requests_handled", []):
            modules[req]["repairs"] += 1

    for entry in autofix_log:
        file = entry.get("file")
        if not file:
            continue
        if entry.get("result") == "Failed":
            fail_count[file] += 1
        modules[file]["autofixes"] += 1

    report = {
        "timestamp": datetime.utcnow().isoformat(),
        "modules_ranked": sorted(modules.items(), key=lambda item: (
            item[1]["repairs"] + item[1]["autofixes"] + fail_count[item[0]]
        ), reverse=True),
        "recommendations": []
    }

    for mod, data in report["modules_ranked"]:
        total_hits = data["repairs"] + data["autofixes"]
        risk = fail_count.get(mod, 0)
        if risk >= 3:
            status = "🔥 PRIORITY REFACTOR"
            escalate_to_gpt(mod)
        elif total_hits > 3:
            status = "⚠️ MONITOR - POSSIBLE STABILITY ISSUE"
        else:
            status = "✅ STABLE"

        report["recommendations"].append({
            "module": mod,
            "total_activity": total_hits,
            "repair_count": data["repairs"],
            "autofix_count": data["autofixes"],
            "failures": risk,
            "status": status
        })

    with open(INSIGHT_OUTPUT, "w") as f:
        json.dump(report, f, indent=2)

    print("[StrategyMapper] 🧠 Strategy mapping completed.")
    print(f"[StrategyMapper] Insight written to: {INSIGHT_OUTPUT}")

def run_strategy_mapper():
    print("[StrategyMapper] 🧭 Starting full strategic review...")
    analyze_trends_and_escalate()
    print("[StrategyMapper] ✅ Strategic evaluation complete.")

if __name__ == "__main__":
    run_strategy_mapper()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():