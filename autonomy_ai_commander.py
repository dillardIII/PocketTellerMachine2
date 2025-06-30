from ghost_env import INFURA_KEY, VAULT_ADDRESS
# autonomy_ai_commander.py
# Routes commands, assigns tasks based on phase and bot focus

from ai_registry import get_active_assistants
from bot_tracker import get_bot_focus, assign_task_to_bot
from core_settings import CURRENT_PHASE

def command_loop():
    """
    Main command routing system.
    Evaluates bot capability and assigns tasks based on system phase.
    """
    print(f"[AI Commander] 📡 Running command loop for phase: {CURRENT_PHASE}")
    bots = get_active_assistants()
    
    for bot in bots:
        focus = get_bot_focus(bot["id"])
        
        # Logic based on phase
        if CURRENT_PHASE == "boot" and focus == "initialization":
            assign_task_to_bot(bot["id"], "start_routine_check")
        
        elif CURRENT_PHASE == "autonomy" and focus == "monitor":
            assign_task_to_bot(bot["id"], "run_surveillance")
        
        elif CURRENT_PHASE == "recovery" and focus == "repair":
            assign_task_to_bot(bot["id"], "scan_errors")

        else:
            assign_task_to_bot(bot["id"], "idle")

    print("[AI Commander] ✅ Task assignment complete.")

def log_event():ef drop_files_to_bridge():