# === FILE: validate_large_json.py ===
# Scans large JSON arrays like self_commands_log.json safely

import json
import sys

if len(sys.argv) < 2:
    print("❌ Usage: python validate_large_json.py <path_to_json_file>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, "r") as f:
        data = json.load(f)

    if isinstance(data, list):
        print(f"🔍 Scanning {len(data)} entries in list...")
        for i, entry in enumerate(data):
            try:
                json.dumps(entry)  # Validate each entry
            except Exception as e:
                print(f"❌ Invalid JSON at entry #{i}: {e}")
                break
        else:
            print(f"✅ File is valid. All entries in list look good.")
    elif isinstance(data, dict):
        print("✅ File is valid JSON object.")
    else:
        print("⚠️ File is valid JSON but neither list nor dict.")
except json.JSONDecodeError as e:
    print(f"❌ JSON decode error: {e}")
except Exception as e:
    print(f"❌ General error: {e}")