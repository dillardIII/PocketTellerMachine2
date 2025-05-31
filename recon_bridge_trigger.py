# recon_bridge_trigger.py

def trigger_recon(target="screeps"):
    """
    Launches the adaptive recon system for a given target.
    Currently defaults to Screeps.
    """
    try:
        print(f"[RECON TRIGGER] Initiating recon mission to: {target}")
        from adaptive_recon_launcher import launch_recon
        result = launch_recon(target)
        print("[RECON TRIGGER] Mission complete.")
        return result
    except Exception as e:
        print(f"[RECON TRIGGER ERROR] Failed to launch recon: {str(e)}")
        return None