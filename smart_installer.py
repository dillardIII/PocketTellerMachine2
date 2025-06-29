# === FILE: smart_installer.py ===

import os
import subprocess
import sys

def smart_install(package):
    try:
        import importlib
        importlib.import_module(package)
        print(f"[SMART INSTALL] ✅ '{package}' already installed.")
    except ImportError:
        print(f"[SMART INSTALL] 🚀 Installing '{package}'...")
        pip_cmd = 'pip' if subprocess.run(['which', 'pip'], capture_output=True).returncode == 0 else 'pip3'
        subprocess.check_call([pip_cmd, 'install', package])

if __name__ == "__main__":
    packages = ["flask"]
    for pkg in packages:
        smart_install(pkg)