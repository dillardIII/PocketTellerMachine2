# === FILE: github_push_pipeline.py ===
# 🌐 Ensures clean pipeline pushes to GitHub, retry on failure.

import subprocess
import time

def safe_push():
    while True:
        try:
            print("[GitPipeline] ⏳ Ensuring branch is up-to-date...")
            subprocess.run(["git", "pull"], check=True)
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "🔄 Automated pipeline sync"], check=True)
            subprocess.run(["git", "push"], check=True)
            print("[GitPipeline] ✅ Pushed to GitHub successfully.")
        except subprocess.CalledProcessError as e:
            print(f"[GitPipeline] ⚠️ Retry after error: {e}")
        time.sleep(600)

if __name__ == "__main__":
    safe_push()