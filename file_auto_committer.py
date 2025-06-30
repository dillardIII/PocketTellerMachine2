from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: file_auto_committer.py ===
# 📦 PTM File Auto-Committer – Handles post-repair Git versioning

import subprocess
import os
from datetime import datetime

def auto_commit_file(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"[AUTO-COMMITTER ERROR] ❌ File not found: {file_path}")
            return {"status": "error", "message": f"File not found: {file_path}"}

        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        commit_message = f"🤖 Auto-commit by PTM Self-Rebuilder: Updated {os.path.basename(file_path)} at {timestamp}"

        # === Stage file ===
        subprocess.run(["git", "add", file_path], check=True)
        # === Commit with message ===
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        # === Push to current branch ===
        subprocess.run(["git", "push"], check=True)

        print(f"[AUTO-COMMITTER] ✅ Committed and pushed {file_path} with message: {commit_message}")
        return {"status": "success", "file": file_path, "message": commit_message}

    except subprocess.CalledProcessError as e:
        print(f"[AUTO-COMMITTER ERROR] ❌ Git command failed: {e}")
        return {"status": "error", "file": file_path, "message": f"Git command failed: {e}"}

    except Exception as e:
        print(f"[AUTO-COMMITTER ERROR] ❌ {e}")
        return {"status": "error", "file": file_path, "message": str(e)}


# === 🔁 Fallback Console Committer (for non-git environments) ===
def console_auto_commit(file_path):
    print(f"[AutoCommitter] 💾 Auto-committed (console only) {file_path}")
    return {"status": "committed", "file": file_path}

def log_event():ef drop_files_to_bridge():