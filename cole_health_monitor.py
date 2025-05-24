import os
import json
import psutil
from datetime import datetime
from assistants.malik import malik_report

HEALTH_LOG_FILE = "data/cole_health_log.json"
HEALTH_ALERT_FILE = "data/cole_health_alerts.json"

# === Threshold Config ===
THRESHOLDS = {
    "cpu_percent": 85,
    "memory_percent": 80,
    "disk_percent": 90,
    "load_avg": 5.0  # For 1-minute load average
}

# === Log Health Snapshot ===
def log_health_snapshot(status):
    logs = []
    if os.path.exists(HEALTH_LOG_FILE):
        try:
            with open(HEALTH_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append(status)
    with open(HEALTH_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Log Health Alerts ===
def log_health_alert(alert):
    alerts = []
    if os.path.exists(HEALTH_ALERT_FILE):
        try:
            with open(HEALTH_ALERT_FILE, "r") as f:
                alerts = json.load(f)
        except:
            alerts = []

    alerts.append(alert)
    with open(HEALTH_ALERT_FILE, "w") as f:
        json.dump(alerts[-500:], f, indent=2)

# === Health Monitor ===
def run_health_monitor():
    print("[Health Monitor] Running system health check...")

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    load_avg = os.getloadavg()[0]  # 1-minute load average
    process_count = len(psutil.pids())

    status = {
        "timestamp": datetime.now().isoformat(),
        "cpu_percent": cpu,
        "memory_percent": memory,
        "disk_percent": disk,
        "load_avg": load_avg,
        "process_count": process_count
    }

    log_health_snapshot(status)

    # === Threshold Checks & Alerts ===
    alert_triggered = False
    alert_message = "[Health Alert] Thresholds breached:\n"

    if cpu > THRESHOLDS["cpu_percent"]:
        alert_triggered = True
        alert_message += f"- CPU Usage: {cpu}% (Threshold: {THRESHOLDS['cpu_percent']}%)\n"

    if memory > THRESHOLDS["memory_percent"]:
        alert_triggered = True
        alert_message += f"- Memory Usage: {memory}% (Threshold: {THRESHOLDS['memory_percent']}%)\n"

    if disk > THRESHOLDS["disk_percent"]:
        alert_triggered = True
        alert_message += f"- Disk Usage: {disk}% (Threshold: {THRESHOLDS['disk_percent']}%)\n"

    if load_avg > THRESHOLDS["load_avg"]:
        alert_triggered = True
        alert_message += f"- Load Avg: {load_avg} (Threshold: {THRESHOLDS['load_avg']})\n"

    if alert_triggered:
        print(alert_message)
        malik_report(alert_message)
        log_health_alert({
            "timestamp": datetime.now().isoformat(),
            "alert": alert_message.strip()
        })
    else:
        print("[Health Monitor] All systems nominal.")

# === CLI Trigger ===
if __name__ == "__main__":
    run_health_monitor()