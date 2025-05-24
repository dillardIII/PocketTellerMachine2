import os
import datetime

# === File Paths ===
GENERATED_CODE_FILE = "data/cole_generated_code.py"
TARGET_APP_FILE = "app.py"
INJECTION_LOG_FILE = "data/cole_injection_log.txt"
BACKUP_FOLDER = "data/backups"

# === Inject Cole's generated code into app.py ===
def inject_code_to_app():
    if not os.path.exists(GENERATED_CODE_FILE):
        print("[Cole Injector] No generated code found.")
        return False

    if not os.path.exists(TARGET_APP_FILE):
        print("[Cole Injector] Target app.py not found.")
        return False

    # Read the generated code
    with open(GENERATED_CODE_FILE, "r") as f:
        generated_code = f.read()

    # Basic check for @app.route
    if "@app.route" not in generated_code:
        print("[Cole Injector] Generated code does not contain a Flask route.")
        return False

    # Create backup folder if not exists
    os.makedirs(BACKUP_FOLDER, exist_ok=True)

    # Backup current app.py
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"{BACKUP_FOLDER}/app_backup_{timestamp}.py"
    with open(TARGET_APP_FILE, "r") as original, open(backup_file, "w") as backup:
        backup.write(original.read())

    # Inject the code at the bottom of app.py
    with open(TARGET_APP_FILE, "a") as app_file:
        app_file.write("\n\n# === Cole Auto-Injected Route ===\n")
        app_file.write(generated_code)
        app_file.write("\n# === End of Cole Injection ===\n")

    # Log the injection
    with open(INJECTION_LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] Injected generated code into {TARGET_APP_FILE}\n")

    print(f"[Cole Injector] Injection complete. Backup created at {backup_file}")
    return True

# === Manual test ===
if __name__ == "__main__":
    inject_code_to_app()