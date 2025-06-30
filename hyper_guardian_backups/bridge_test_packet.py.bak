# === FILE: bridge_test_packet.py ===
# 🧪 Bridge Test Packet – Writes a test file to inbox for pickup verification.

import os
import time

def drop_test_packet():
    test_folder = "bridge/inbox"
    os.makedirs(test_folder, exist_ok=True)  # Ensure folder exists

    filename = os.path.join(test_folder, "test_packet.txt")
    content = f"This is a test packet.\nTimestamp: {time.ctime()}"

    try:
        with open(filename, "w") as f:
            f.write(content)
        print(f"[Bridge Test] ✅ Test packet dropped: {filename}")
    except Exception as error:
        print(f"[Bridge Test] ❌ Failed to drop packet: {error}")

if __name__ == "__main__":
    drop_test_packet()