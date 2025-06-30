"""
Sovereign Logic Chain
Core processor for PTM's self-directing AI logic.
Generates its own tasks based on prior output, ethics, goals, and detected opportunity fields.
"""

import json
from datetime import datetime

LOGIC_CHAIN_LOG = "memory/sovereign_logic_log.json"

def generate_next_objective(previous_result, active_context, ethics_constraints):
    """
    Uses recursive priority logic and historical context to produce the next task.
    """
    if not previous_result:
        return "initialize_self_check"

    if "error" in previous_result.lower():
        return "invoke_self_diagnosis"

    if "success" in previous_result.lower() and "data" in active_context.lower():
        return "expand_data_analysis"

    if ethics_constraints.get("avoid_risk") and "volatile" in active_context:
        return "alert_user_for_override"

    return "evolve_next_module"

def log_chain_step(input_data, decision):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "input": input_data,
        "decision": decision
    }

    try:
        with open(LOGIC_CHAIN_LOG, "r") as f:
            history = json.load(f)
    except:
        history = []

    history.append(entry)

    with open(LOGIC_CHAIN_LOG, "w") as f:
        json.dump(history[-100:], f, indent=2)

def run_logic_chain(previous_result, context, ethics):
    decision = generate_next_objective(previous_result, context, ethics)
    log_chain_step({
        "result": previous_result,
        "context": context,
        "ethics": ethics
    }, decision)
    return decision