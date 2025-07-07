#!/bin/bash
# === FILE: boot_autostart.sh ===

export OPENAI_API_KEY="sk-..."  # <-- PUT YOUR KEY HERE
cd /home/runner/workspace  # Or your project directory
nohup python3 self_launcher.py &
echo "[BootAutoStart] 🚀 PTM Empire has been launched in the background."