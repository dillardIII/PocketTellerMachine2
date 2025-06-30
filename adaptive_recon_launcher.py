from ghost_env import INFURA_KEY, VAULT_ADDRESS
# adaptive_recon_launcher.py

def launch_recon(target="screeps"):
    """
    Attempts to launch a recon mission using the best available recon tool.
    Priority: selenium_wire → playwright → puppeteer → fallback
    """
    print(f"[GHOSTSHADE] Starting recon to: {target}")

    # STEP 1: Try Selenium-Wire
    try:
        from selenium_wire_agent import run_selenium_recon
        print("[GHOSTSHADE] Using selenium_wire_agent.")
        return run_selenium_recon(target)
    except Exception as e1:
        print(f"[GHOSTSHADE] Selenium failed: {str(e1)}")

    # STEP 2: Try Playwright (JS)
    try:
        import subprocess
        print("[GHOSTSHADE] Falling back to Playwright agent.")
        result = subprocess.run(["node", "playwright_agent.js"], capture_output=True, text=True)
        print(result.stdout)
        return result.stdout
    except Exception as e2:
        print(f"[GHOSTSHADE] Playwright failed: {str(e2)}")

    # STEP 3: Try Puppeteer
    try:
        print("[GHOSTSHADE] Trying Puppeteer agent.")
        result = subprocess.run(["node", "puppeteer_agent.js"], capture_output=True, text=True)
        print(result.stdout)
        return result.stdout
    except Exception as e3:
        print(f"[GHOSTSHADE] Puppeteer failed: {str(e3)}")

    # STEP 4: Hard fallback (future: PyAutoGUI, TagUI, MacroDroid relay)
    print("[GHOSTSHADE] All recon tools failed. No mission executed.")
    return None

def log_event():ef drop_files_to_bridge():