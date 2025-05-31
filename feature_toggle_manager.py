# Feature Toggle Manager
toggles = {
    "voice_enabled": True,
    "strategy_autogen": True,
    "real_trade_mode": False
}

def toggle_feature(name, state):
    toggles[name] = state
    print(f"[FeatureToggle] {name} set to {state}")

def is_enabled(name):
    return toggles.get(name, False)