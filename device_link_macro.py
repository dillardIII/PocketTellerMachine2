# === FILE: device_link_macro.py ===
import os

def check_usb_devices():
    print("[LinkMacro] Checking connected USB devices...\n")
    os.system("adb devices")

if __name__ == "__main__":
    check_usb_devices()