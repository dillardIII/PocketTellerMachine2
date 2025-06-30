# 📝 Auto File Writer + Git Committer + GitHub Pusher
import os
import subprocess
from datetime import datetime

def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    print(f"[AutoWriter] 📝 Wrote file: {filename}")

def git_commit_push(filename, message=None):
    try:
        if not message:
            message = f"Auto update {filename} at {datetime.utcnow().isoformat()}"

        subprocess.run(["git", "add", filename], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push"], check=True)

        print(f"[GitPusher] 🚀 Committed & pushed: {filename}")
    except subprocess.CalledProcessError as e:
        print(f"[GitPusher] ❌ Git command failed: {e}")

if __name__ == "__main__":
    # Example usage
    filename = "dynamic_strategy.py"
    content = "print('This is an auto-generated trading strategy.')"
    write_file(filename, content)
    git_commit_push(filename)