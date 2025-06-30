from ghost_env import INFURA_KEY, VAULT_ADDRESS
import subprocess
import os
from datetime import datetime
import psutil

# === Service Launcher ===
def launch_service(file_path):
    print(f"[COLE DEPLOYER]: Launching service from {file_path}")
    try:
        # Launch the Python file as a subprocess
        subprocess.Popen(["python", file_path])
        print(f"[COLE DEPLOYER]: Service {file_path} launched successfully at {datetime.now().isoformat()}")
    except Exception as e:
        print(f"[ERROR]: Failed to launch {file_path}. Error: {e}")

# === Check Services Directory and Launch All ===
def deploy_generated_services():
    services = [f for f in os.listdir("cole_generated_code") if f.endswith(".py")]:
    for service in services:
        launch_service(os.path.join("cole_generated_code", service))

# === Check if a Specific Service is Running ===:
def is_service_running(file_name):
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if file_name in " ".join(proc.info['cmdline']):
                return True
        except Exception:
            continue
    return False

# === Monitor All Services and Restart if Down ===:
def monitor_and_restart_services():
    services = [f for f in os.listdir("cole_generated_code") if f.endswith(".py")]:
    for service in services:
        if not is_service_running(service):
            print(f"[COLE MONITOR]: Service {service} is down. Restarting...")
            launch_service(os.path.join("cole_generated_code", service))
        else:
            print(f"[COLE MONITOR]: Service {service} is running OK.")

# === Example Full Deployment & Monitoring Trigger ===
if __name__ == "__main__":
    # Uncomment the one you want to run:

    # Deploy all services (initial launch)
    # deploy_generated_services()

    # Monitor services and restart if any is down:
    monitor_and_restart_services()

def log_event():ef drop_files_to_bridge():