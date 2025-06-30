# === FILE: smart_file_auditor.py ===

# 🧠 SmartFile Auditor – Scans PTM directories for missing, outdated, or corrupted files.
# Coordinates with InspectorBot and GhostForge to request replacements, corrections, or upgrades.

import os
import json
import hashlib
from datetime import datetime

# === Configurable Audit Settings ===
AUDIT_LOG_PATH = "logs/smart_file_audit_log.json"
EXPECTED_FILES_PATH = "config/expected_files.json"
GHOSTFORGE_REQUEST_PATH = "requests/ghostforge_repair_requests.json"
AUDIT_SCOPE_DIRS = ["core", "ui", "vault", "bots", "assistants", "agents"]

def get_file_hash(filepath):
    """Generate SHA-256 hash of a file for integrity check."""
    try:
        with open(filepath, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except:
        return None

def load_expected_files():
    """Load the expected files and their checksums or metadata from the config file."""
    try:
        with open(EXPECTED_FILES_PATH, "r") as f:
            return json.load(f)
    except:
        return {}

def log_audit_result(results):
    """Write audit results to the audit log with a timestamp."""
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {
        "timestamp": timestamp,
        "results": results
    }

    os.makedirs(os.path.dirname(AUDIT_LOG_PATH), exist_ok=True)

    try:
        if os.path.exists(AUDIT_LOG_PATH):
            with open(AUDIT_LOG_PATH, "r") as f:
                log = json.load(f)
        else:
            log = []

        log.append(log_entry)

        with open(AUDIT_LOG_PATH, "w") as f:
            json.dump(log, f, indent=2)

    except Exception as e:
        print(f"[SmartFileAuditor] Failed to write audit log: {e}")

def queue_ghostforge_request(broken_files):
    """Queue a repair or rebuild request for missing/corrupt files."""
    os.makedirs(os.path.dirname(GHOSTFORGE_REQUEST_PATH), exist_ok=True)
    
    request = {
        "timestamp": datetime.utcnow().isoformat(),
        "request_type": "file_repair",
        "files": broken_files
    }

    try:
        if os.path.exists(GHOSTFORGE_REQUEST_PATH):
            with open(GHOSTFORGE_REQUEST_PATH, "r") as f:
                requests = json.load(f)
        else:
            requests = []

        requests.append(request)

        with open(GHOSTFORGE_REQUEST_PATH, "w") as f:
            json.dump(requests, f, indent=2)

        print(f"[SmartFileAuditor] Queued {len(broken_files)} file(s) for GhostForge repair.")
    except Exception as e:
        print(f"[SmartFileAuditor] Failed to queue GhostForge request: {e}")

def run_audit():
    """Main function to run a full audit against expected files."""
    print("[SmartFileAuditor] 🔍 Starting file audit...")
    expected = load_expected_files()
    results = {
        "missing": [],
        "corrupted": [],
        "outdated": [],
        "verified": []
    }

    for rel_path, expected_info in expected.items():
        abs_path = os.path.join(".", rel_path)
        expected_hash = expected_info.get("sha256")
        required = expected_info.get("required", True)

        if not os.path.exists(abs_path):
            if required:
                results["missing"].append(rel_path)
            continue

        current_hash = get_file_hash(abs_path)
        if current_hash is None:
            results["corrupted"].append(rel_path)
        elif expected_hash and current_hash != expected_hash:
            results["outdated"].append(rel_path)
        else:
            results["verified"].append(rel_path)

    log_audit_result(results)

    if results["missing"] or results["corrupted"] or results["outdated"]:
        broken = results["missing"] + results["corrupted"] + results["outdated"]
        queue_ghostforge_request(broken)
    else:
        print("[SmartFileAuditor] ✅ All files passed audit.")

    return results

# === Run Audit Automatically if Called Directly ===
if __name__ == "__main__":
    audit_results = run_audit()
    print(json.dumps(audit_results, indent=2))