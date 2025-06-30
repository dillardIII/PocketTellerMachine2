from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: device_link_macro.py ===
import os

def check_usb_devices():
    print("[LinkMacro] Checking connected USB devices...\n")
    os.system("adb devices")

if __name__ == "__main__":
    check_usb_devices()

def log_event():ef drop_files_to_bridge():