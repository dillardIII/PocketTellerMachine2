import os
import json

DATA_DIR = "data"

def debug_json_files():
    issues = []
    files = os.listdir(DATA_DIR)

    print("=== JSON DEBUGGER: Checking files in /data ===")
    for fname in files:
        if not fname.endswith(".json"):
            continue

        path = os.path.join(DATA_DIR, fname)

        try:
            with open(path, "r") as f:
                content = f.read()
                if not content.strip():
                    raise ValueError("File is empty")
                json.loads(content)
        except Exception as e:
            issues.append((fname, str(e)))
            print(f"[ERROR] {fname} — {e}")
        else:
            print(f"[OK] {fname}")

    if not issues:
        print("\n✅ All JSON files are valid.\n")
    else:
        print("\n⚠️ Issues detected in the following files:\n")
        for fname, error in issues:
            print(f"  - {fname}: {error}")

    return issues

# Run this directly to scan your /data files
if __name__ == "__main__":
    debug_json_files()