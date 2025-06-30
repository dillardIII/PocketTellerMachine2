from ghost_env import INFURA_KEY, VAULT_ADDRESS
# feature_toggle_manager.py – Feature Flags Controller

# Feature toggles (manually adjustable or dynamically set)
FEATURE_FLAGS = {
    "strategy_autogen": True,
    "mood_engine": True,
    "voice_recap": False,
    "recon_scraper": True,
    "vps_controller": True
}

def is_enabled(feature_name):
    enabled = FEATURE_FLAGS.get(feature_name, False)
    print(f"[Feature Toggle] {feature_name} is {'enabled' if enabled else 'disabled'}."):
    return enabled

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():