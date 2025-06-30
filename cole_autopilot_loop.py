from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import time
import random
from datetime import datetime

# === Core Autonomy Functions ===
from cole_task_queue import add_task
from cole_code_writer import cole_write_code, cole_write_code_gpt
from cole_brain import cole_think, run_decision_cycle
from cole_task_optimizer import cole_optimize_tasks
from cole_congress_tracker import run_congress_ai_tracker
from cole_congress_sentiment_overlay import fetch_congress_sentiment
from cole_sentiment_weighted_trade_trigger import run_sentiment_weighted_trade_trigger
from cole_trade_decision_engine import run_trade_decision_engine
from cole_trigger_rules import run_trigger_rules_check
from cole_self_healing_error_watcher import run_self_healing_autofix
from cole_auto_correction_loop import run_auto_correction_failsafe
from cole_smart_analytics import run_smart_analytics
from cole_performance_review import run_performance_review
from cole_health_monitor import check_health
from cole_smart_recovery import run_smart_recovery
from cole_emergency_cooldown import recover_if_cooldown_passed
from cole_phase_manager import auto_detect_phase, get_current_phase, detect_phase, set_phase
from cole_tools.cole_auto_runner import cole_auto_run
from cole_tools.gpt_advisor import ask_gpt, get_phase_advice, get_task_list, get_strategy_note
from assistants.malik import malik_report
from cole_logger import log_info

# === Memory Paths ===
AUTOLOG_FILE = "data/cole_autopilot_log.json"
ESCALATION_STATE_FILE = "data/cole_recovery_escalation.json"
BRAIN_MEMORY_FILE = "data/cole_brain_memory.json"

# === Logging ===
def log_autopilot_action(action, detail):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "detail": detail
    }

    logs = []
    if os.path.exists(AUTOLOG_FILE):
        try:
            with open(AUTOLOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append(entry)
    with open(AUTOLOG_FILE, "w") as f:
        json.dump(logs[-300:], f, indent=2)

    print(f"[Autopilot] {action}: {detail}")

def save_brain_memory(thought):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "thought": thought
    }

    memory = []
    if os.path.exists(BRAIN_MEMORY_FILE):
        try:
            with open(BRAIN_MEMORY_FILE, "r") as f:
                memory = json.load(f)
        except:
            memory = []

    memory.append(entry)
    with open(BRAIN_MEMORY_FILE, "w") as f:
        json.dump(memory[-300:], f, indent=2)

def is_emergency_mode():
    if os.path.exists(ESCALATION_STATE_FILE):
        try:
            with open(ESCALATION_STATE_FILE, "r") as f:
                state = json.load(f)
            return state.get("level", 0) >= 3
        except:
            pass
    return False

# === Autopilot Core Cycle ===
def cole_autopilot_cycle(context=None):
    now = datetime.now()
    print(f"[{now}] Cole: Starting Full Autopilot Cycle...")
    log_info("Cole: Starting Full Autopilot Cycle...")

    cole_auto_run(context)

    # Phase Logic
    current_phase = detect_phase()
    set_phase(current_phase)
    log_info(f"[Phase Manager] Current Market Phase: {current_phase}")
    malik_report(f"[Phase Manager] Current Market Phase: {current_phase}")

    try:
        insight = get_phase_advice(f"What advice do you have for Cole's current phase: {current_phase}?")
        if isinstance(insight, str):
            log_autopilot_action("GPT Insight", insight)
            malik_report(f"[GPT Insight] {insight}")
            save_brain_memory(insight)
        else:
            log_autopilot_action("GPT Insight Error", "GPT did not return a string")
    except Exception as e:
        log_autopilot_action("GPT Insight Error", str(e))

    # Recovery Mode
    if recover_if_cooldown_passed():
        malik_report("[Cooldown Recovery] Emergency mode exited after healthy streak.")

    run_smart_recovery()

    if is_emergency_mode():
        log_autopilot_action("Emergency Mode", "Escalation Level 3 detected.")
        malik_report("[Emergency Mode] Essential modules only.")
        health_report = check_health()
        malik_report(f"[Health Check] {health_report}")
        return

    # Task + Strategy Execution
    try:
        print("[Autopilot] Generating new tasks...")
        task_json = get_task_list("Generate 5 new tasks to improve the trading strategy, data visualization, and risk management of the Cole AI system. Return as a JSON list.")
        if isinstance(task_json, list):
            from cole_phase_manager import phase_task_filter
            filtered = phase_task_filter(task_json, current_phase)
            for task in filtered:
                if isinstance(task, str) and add_task(task):
                    log_autopilot_action("Task Generated", task)
        else:
            log_autopilot_action("Task Generation Error", "Invalid task format.")
    except Exception as e:
        log_autopilot_action("Task Generation Error", str(e))

    try:
        note = get_strategy_note("Write a technical strategy note for Cole AI regarding trade entry criteria using support and resistance levels with RSI confirmation.")
        if note:
            filename = f"data/logic_note_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, "w") as f:
                f.write(note)
            log_autopilot_action("Logic Note Created", filename)
            malik_report(f"Cole updated logic notes at {filename}")
    except Exception as e:
        log_autopilot_action("Logic Note Error", str(e))

    cole_optimize_tasks()
    run_congress_ai_tracker()
    fetch_congress_sentiment()
    run_sentiment_weighted_trade_trigger()
    run_trade_decision_engine()
    run_trigger_rules_check()
    run_self_healing_autofix()
    run_auto_correction_failsafe()
    run_smart_analytics()
    run_performance_review()
    run_decision_cycle()

    # Health Check
    health_report = check_health()
    malik_report(f"[Health Check] {health_report}")

    # Code Generation (Autonomous)
    try:
        task_list = [
            "RSI Strategy Generator",
            "EMA Crossover Analyzer",
            "Momentum Screener Bot",
            "MACD Signal Scanner",
            "Bollinger Bands Alert System"
        ]
        selected_task = random.choice(task_list)
        use_gpt = random.choice([True, False])

        if use_gpt:
            malik_report("[Autopilot] Using GPT mode for code generation.")
            code = cole_write_code_gpt(selected_task)
            file_path = f"data/generated_gpt_{selected_task.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(file_path, "w") as f:
                f.write(code)
            log_autopilot_action("Code Generated (GPT)", file_path)
            malik_report(f"[GPT Code] Saved to {file_path}")
        else:
            malik_report("[Autopilot] Using template mode for code generation.")
            path = cole_write_code(selected_task, description="Autopilot fallback mode")
            log_autopilot_action("Code Generated (Template)", path)
            malik_report(f"[Template Code] Saved to {path}")
    except Exception as e:
        log_autopilot_action("Code Generation Error", str(e))

    print(f"[{datetime.now()}] Cole: Autopilot cycle completed.")
    log_info("Cole: Autopilot cycle completed.")

if __name__ == "__main__":
    cole_autopilot_cycle()

def log_event():ef drop_files_to_bridge():