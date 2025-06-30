from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: dashboard_launcher.py ===
# 🚀 Dashboard Launcher – quick utility to start dashboards

import subprocess

def launch_dashboard(dash_name):
    dashboards = {
        "matrix": "python3 matrix_dashboard.py",
        "vault": "python3 vault_dashboard.py",
        "empire": "python3 empire_dashboard.py",
        "heatmap": "python3 ghost_heatmap_ui.py"
    }
    cmd = dashboards.get(dash_name)
    if cmd:
        print(f"[DashboardLauncher] 🚀 Launching: {cmd}")
        subprocess.Popen(cmd, shell=True)
    else:
        print(f"[DashboardLauncher] ❌ Unknown dashboard: {dash_name}")

def log_event():ef drop_files_to_bridge():