from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: assistant_comms_matrix.py ===
"""
Assistant Communication Matrix:
Defines which assistants are allowed to communicate with each other
and what types of messages they can send (review, escalate, request).
This is the master permission map for the PTM bot network.
"""

COMMS_RULES = {
    "MoCash": {
        "allowed_targets": ["Mentor", "Strategist", "DrillInstructor", "ChillTrader"],
        "allowed_tasks": ["review", "escalate", "suggest"]
    },
    "Mentor": {
        "allowed_targets": ["Strategist", "MoCash", "DrillInstructor"],
        "allowed_tasks": ["review", "comment", "support"]
    },
    "Strategist": {
        "allowed_targets": ["Mentor", "MoCash"],
        "allowed_tasks": ["approve", "reject", "optimize"]
    },
    "DrillInstructor": {
        "allowed_targets": ["MoCash", "Mentor"],
        "allowed_tasks": ["warn", "flag", "retrain"]
    },
    "ChillTrader": {
        "allowed_targets": ["MoCash", "Mentor"],
        "allowed_tasks": ["comment", "warn"]
    }
}

def can_send(sender, receiver, task):
    """
    Returns True if sender is allowed to message receiver with that task type.:
    """
    sender_rules = COMMS_RULES.get(sender)
    if not sender_rules:
        return False
    return receiver in sender_rules["allowed_targets"] and task in sender_rules["allowed_tasks"]

# === Local test ===
if __name__ == "__main__":
    print("Can MoCash review Mentor?", can_send("MoCash", "Mentor", "review"))     # ✅
    print("Can ChillTrader escalate to MoCash?", can_send("ChillTrader", "MoCash", "escalate"))  # ❌

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():