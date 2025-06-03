# === FILE: recon_agent.py ===
# 🛰️ Recon Agent – Monitors system environment, detects threats, scans conditions, and reports observations

import time
import random

class ReconAgent:
    def __init__(self):
        self.status_log = []
        print("[ReconAgent] Online and watching.")

    def run_recon_loop(self):
        while True:
            # Perform a simulated recon check
            scan = self._perform_scan()
            self.status_log.append(scan)
            print(f"[ReconAgent] Logged system scan: {scan}")
            time.sleep(20)

    def _perform_scan(self):
        recon_types = [
            "Connection Health",
            "File Integrity",
            "Resource Load",
            "Bridge Stability",
            "Memory Usage",
            "Unauthorized Access Check",
        ]
        result = {
            "scan_type": random.choice(recon_types),
            "status": random.choice(["OK", "WARNING", "FAIL"]),
            "timestamp": time.ctime()
        }
        return result

    def get_latest_status(self):
        if not self.status_log:
            return None
        return self.status_log[-1]