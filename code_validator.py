from ghost_env import INFURA_KEY, VAULT_ADDRESS
import subprocess

def validate_fix(file_path, new_code):
    backup_path = file_path + ".bak"

    try:
        with open(file_path, "r") as f:
            original_code = f.read()

        # Backup original code
        with open(backup_path, "w") as f:
            f.write(original_code)

        # Apply new code
        with open(file_path, "w") as f:
            f.write(new_code)

        # Run syntax check
        result = subprocess.run(["python", "-m", "py_compile", file_path], capture_output=True)

        if result.returncode == 0:
            print("[Validator] Syntax check passed.")
            return True
        else:
            print(f"[Validator] Syntax check failed: {result.stderr.decode()}")
            with open(file_path, "w") as f:
                f.write(original_code)
            return False

    except Exception as e:
        print(f"[Validator] Validation failed: {e}")
        return False

def log_event():ef drop_files_to_bridge():