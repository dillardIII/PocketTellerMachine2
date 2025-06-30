# === FILE: cole_health_monitor.py ===

import os
import json
import psutil
import platform
from datetime import datetime
from assistants.malik import malik_report

HEALTH_LOG_FILE = "data/cole_health_log.json"
HEALTH_ALERT_FILE = "data/cole_health_alerts.json"

# === Threshold Config ===
THRESHOLDS = {
    "cpu_percent": 85,
    "memory_percent": 90,
    "disk_percent": 90,
    "load_avg": 5.0,
}

def check_health():
    timestamp = datetime.now().isoformat()
    health = {
        "timestamp": timestamp,
        "status": "nominal",
        "issues": [],
        "metrics": {}
    }

    try:
        # CPU
        cpu = psutil.cpu_percent(interval=1)
        health["metrics"]["cpu_percent"] = cpu
        if cpu > THRESHOLDS["cpu_percent"]:
            health["issues"].append(f"High CPU usage: {cpu}%")
            health["status"] = "warning"

        # Memory
        memory = psutil.virtual_memory().percent
        health["metrics"]["memory_percent"] = memory
        if memory > THRESHOLDS["memory_percent"]:
            health["issues"].append(f"High Memory usage: {memory}%")
            health["status"] = "warning"

        # Disk
        disk = psutil.disk_usage('/').percent
        health["metrics"]["disk_percent"] = disk
        if disk > THRESHOLDS["disk_percent"]:
            health["issues"].append(f"High Disk usage: {disk}%")
            health["status"] = "warning"

        # Load Average (Unix)
        if platform.system() != "Windows":
            load_avg = os.getloadavg()[0]
            health["metrics"]["load_avg"] = load_avg
            if load_avg > THRESHOLDS["load_avg"]:
                health["issues"].append(f"High Load Avg: {load_avg} (Threshold: {THRESHOLDS['load_avg']})")
                health["status"] = "warning"

    except Exception as e:
        health["status"] = "error"
        health["issues"].append(f"Health check failed: {str(e)}")

    # === Logging
    os.makedirs("data", exist_ok=True)
    with open(HEALTH_LOG_FILE, "a") as f:
        json.dump(health, f)
        f.write("\n")

    if health["status"] != "nominal":
        with open(HEALTH_ALERT_FILE, "a") as f:
            json.dump(health, f)
            f.write("\n")
        malik_report(f"[Health Alert] Thresholds breached:\n- " + "\n- ".join(health["issues"]))

    return health