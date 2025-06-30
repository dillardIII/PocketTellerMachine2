from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: auto_tester.py ===
# 🧪 PTM Auto Tester – Runs test cases to verify stability after code patch

import subprocess
import os

def run_basic_tests(target_path):
    """
    Runs basic syntax check and test suite (if available) on the file.:
:
    Args:
        target_path (str): File path of the patched code

    Returns:
        dict: test results including status, stdout, and stderr
    """
    if not os.path.exists(target_path):
        return {"status": "file_missing", "file": target_path}

    print(f"[AUTO TESTER] 🚦 Testing patched file: {target_path}")

    # Syntax check
    try:
        syntax_cmd = ["python3", "-m", "py_compile", target_path]
        syntax_result = subprocess.run(
            syntax_cmd, capture_output=True, text=True, timeout=10
        )

        if syntax_result.returncode != 0:
            print("[AUTO TESTER] ❌ Syntax error found.")
            return {
                "status": "syntax_error",
                "file": target_path,
                "stderr": syntax_result.stderr
            }

        print("[AUTO TESTER] ✅ Syntax OK.")

    except Exception as e:
        return {"status": "test_failed", "error": str(e)}

    # Optional: Custom test logic
    test_file = f"tests/test_{os.path.basename(target_path)}"
    if os.path.exists(test_file):
        try:
            print(f"[AUTO TESTER] 🧪 Running test: {test_file}")
            test_cmd = ["python3", test_file]
            test_result = subprocess.run(
                test_cmd, capture_output=True, text=True, timeout=15
            )

            if test_result.returncode != 0:
                return {
                    "status": "test_failed",
                    "file": target_path,
                    "stderr": test_result.stderr
                }

            print("[AUTO TESTER] ✅ All tests passed.")
            return {
                "status": "passed",
                "file": target_path,
                "stdout": test_result.stdout
            }

        except Exception as e:
            return {"status": "test_crashed", "error": str(e)}
    else:
        print("[AUTO TESTER] ⚠️ No test file found. Assuming success.")
        return {"status": "passed", "file": target_path, "stdout": "No tests run."}

def log_event():ef drop_files_to_bridge():