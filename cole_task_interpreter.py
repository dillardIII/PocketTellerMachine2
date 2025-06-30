from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_task_interpreter.py

import json
import os
from datetime import datetime

# === Import task modules ===
from cole_code_writer import cole_write_code
from cole_executor import run_trade_with_strategy
from cole_backtester import run_backtest
from cole_analysis import run_analysis
from cole_self_healing_error_watcher import run_self_healing_autofix

# === Logging path ===
TASK_LOG_FILE = "logs/task_trace_log.json"

def log_task_trace(task, tags):
    os.makedirs("logs", exist_ok=True)
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "task": task,
        "tags": tags
    }

    if os.path.exists(TASK_LOG_FILE):
        with open(TASK_LOG_FILE, "r") as f:
            try:
                log_data = json.load(f)
            except:
                log_data = []
    else:
        log_data = []

    log_data.append(log_entry)

    with open(TASK_LOG_FILE, "w") as f:
        json.dump(log_data, f, indent=2)

def interpret_task(task):
    """
    Interprets and routes a task to the proper handler.
    Returns a dictionary with status and task type.
    """
    interpretation = {
        "task_type": None,
        "strategy": None,
        "code_required": False,
        "analysis_required": False,
        "description": "",
        "params": {}
    }

    if not isinstance(task, dict):
        try:
            task = json.loads(task)
        except Exception as e:
            return {"error": f"Invalid task format: {e}"}

    description = task.get("description", "").lower()
    interpretation["description"] = description

    if "generate" in description and "strategy" in description:
        interpretation["task_type"] = "generate_strategy"
        interpretation["code_required"] = True
    elif "analyze" in description or "evaluate" in description:
        interpretation["task_type"] = "analyze"
        interpretation["analysis_required"] = True
    elif "trade" in description or "execute" in description:
        interpretation["task_type"] = "execute_trade"
        interpretation["strategy"] = task.get("strategy", "unknown")
    elif "backtest" in description:
        interpretation["task_type"] = "backtest"
        interpretation["strategy"] = task.get("strategy", "unknown")
    elif "fix" in description or "repair" in description:
        interpretation["task_type"] = "self_heal"
    else:
        interpretation["task_type"] = "unknown"

    interpretation["params"] = task.get("params", {})

    # === Log Tags ===
    tags = [interpretation["task_type"], interpretation["strategy"], *interpretation["params"].keys()]
    log_task_trace(task, tags)

    # === Dispatch to correct handler ===
    task_type = interpretation["task_type"]
    result = {"status": "not executed", "task_type": task_type}

    try:
        if task_type == "generate_strategy":
            result["output"] = cole_write_code(task)
            result["status"] = "executed"
        elif task_type == "analyze":
            result["output"] = run_analysis(task)
            result["status"] = "executed"
        elif task_type == "execute_trade":
            result["output"] = run_trade_with_strategy(task["strategy"], task.get("params", {}))
            result["status"] = "executed"
        elif task_type == "backtest":
            result["output"] = run_backtest(task["strategy"], task.get("params", {}))
            result["status"] = "executed"
        elif task_type == "self_heal":
            result["output"] = run_self_healing_autofix()
            result["status"] = "executed"
        else:
            result["output"] = "Unknown task type. No action taken."
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)

    return result

# === Optional: Test block ===
if __name__ == "__main__":
    test_task = {
        "description": "Generate a new RSI strategy.",
        "params": {"indicator": "RSI", "threshold": 70}
    }
    response = interpret_task(test_task)
    print(json.dumps(response, indent=2))

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():