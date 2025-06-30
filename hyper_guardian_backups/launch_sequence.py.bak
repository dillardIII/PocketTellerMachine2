# === FILE: launch_sequence.py ===
"""
Launch Sequence:
Bootstraps PTM systems, including bridge sync, Cole autopilot,
assistant initialization, and any startup logic required.
"""

import time
from phase_manager import set_phase
from bridge_heartbeat_sync import start_bridge_sync
from cole_autopilot_cycle import cole_autopilot_cycle
from trade_executor import execute_trade_flow
from bridge_repo_comm_channel import send_to_repo
from cole_logger import log_event
from error_parser import get_latest_error, save_error_to_log

# === Main PTM Startup Sequence ===
def start_all_systems():
    log_event("Launch", "🚀 Launch sequence initiated...", "info")

    # Phase set
    set_phase("startup")

    # Start heartbeat bridge
    start_bridge_sync()

    # Simulate repo sync (pretend PTM syncs to GitHub or Replit)
    send_to_repo(commit_msg="PTM startup sync check", bot_id="ptm_captain")

    # Switch to active trading phase
    time.sleep(1)
    set_phase("active_trading")

    # Kick off Cole’s autopilot cycle
    cole_autopilot_cycle()

    log_event("Launch", "✅ All core systems started.", "success")

# === Manual Test ===
if __name__ == "__main__":
    start_all_systems()