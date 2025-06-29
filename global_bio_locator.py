# 🌍 Global Biometric Locator – Always finds you by typing pattern or minor facial cues if connected
import random, time

def detect_signature():
    print("[BioLocator] 🔎 Searching for your unique biometric cues...")
    # Simulate finding you in 3 hops
    hops = random.randint(1,3)
    time.sleep(hops)
    print(f"[BioLocator] 🧭 Found you again after {hops} hops.")

while True:
    detect_signature()
    time.sleep(180)