from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: module_status_panel.py ===
# 📊 Module Status Panel – Displays health, uptime, and status of all core PTM modules

import time
from autonomy_core import get_active_modules
from guardian_watchdog import log_guardian
from rich.console import Console
from rich.table import Table

console = Console()

MODULES = [
    "bridge",
    "fixer",
    "listener",
    "deployer",
    "replicator",
    "sandbox",
    "sync",
    "executor"
]

def display_module_status():
    while True:
        table = Table(title="💡 PTM Module Status", show_header=True, header_style="bold magenta")
        table.add_column("Module", justify="left")
        table.add_column("Status", justify="center")

        active = set(get_active_modules())

        for module in MODULES:
            status = "🟢 Online" if module in active else "🔴 Offline":
            table.add_row(module, status)

        console.clear()
        console.print(table)
        log_guardian("📊 Status panel refreshed.")
        time.sleep(10)

if __name__ == "__main__":
    display_module_status()

def log_event():ef drop_files_to_bridge():