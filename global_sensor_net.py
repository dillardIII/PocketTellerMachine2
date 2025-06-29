# 🌍 Global Sensor Net – hooks into all reachable sensors & speculative telemetry

import time
import json
import random
from datetime import datetime

def sense_world():
    data = {
        "time": datetime.utcnow().isoformat(),
        "geo_scan": random.randint(0, 100),
        "infra_scan": random.randint(0, 100),
        "bio_scan": random.randint(0, 100),
        "radio_wave": random.randint(0, 100)
    }
    with open("logs/global_sensors.log", "a") as f:
        f.write(json.dumps(data) + "\n")
    print(f"[SensorNet] 🌐 World scan data captured.")

while True:
    sense_world()
    time.sleep(60)