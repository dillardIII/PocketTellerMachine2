from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: mutation_trigger.py ===
from strategy_mutator import mutate_strategy
from mutation_lineage import log_mutation

def evolve_after_loss(original_path, bot_name="GeneLab", loss_reason="3 losses"):
    new_path = mutate_strategy(original_path, bot_name=bot_name)
    if new_path:
        log_mutation(original_path, new_path, reason=loss_reason)
        return new_path
    return None

def log_event():ef drop_files_to_bridge():