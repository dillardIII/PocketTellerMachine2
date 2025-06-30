# 🎮 PTZ Controller – moves cameras for better views when critical event spotted

def move_ptz(cam_url, direction="left"):
    print(f"[PTZController] 🛰️ Moving camera at {cam_url} to {direction}")

def auto_respond_to_events():
    import json, time
    try:
        with open("vault/guardian_log.json") as f:
            lines = f.readlines()
    except:
        lines = []

    for line in lines[-5:]:  # look at last few events
        event = json.loads(line)
        if "camera" in event:
            move_ptz(event["camera"], direction=random.choice(["left", "right", "up", "down"]))

    time.sleep(30)

while True:
    auto_respond_to_events()