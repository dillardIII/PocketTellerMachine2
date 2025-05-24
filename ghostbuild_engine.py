import os
import json
from datetime import datetime
from cole_brain import cole_think
from cole_code_injector import inject_generated_code

GHOSTBUILD_LOG = "data/ghostbuild_log.json"
GHOSTBUILD_FOLDER = "cole_generated_code"

os.makedirs(GHOSTBUILD_FOLDER, exist_ok=True)
os.makedirs("data", exist_ok=True)

def ghostbuild_task(prompt, filename=None, inject=True):
    print(f"[GhostBuild] Thinking on: {prompt}")
    
    code = cole_think(prompt)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = filename or f"ghost_{timestamp}.py"
    full_path = os.path.join(GHOSTBUILD_FOLDER, filename)

    try:
        with open(full_path, "w") as f:
            f.write(code)

        log_entry = {
            "timestamp": timestamp,
            "prompt": prompt,
            "file": full_path
        }

        if os.path.exists(GHOSTBUILD_LOG):
            with open(GHOSTBUILD_LOG, "r") as f:
                logs = json.load(f)
        else:
            logs = []

        logs.append(log_entry)
        with open(GHOSTBUILD_LOG, "w") as f:
            json.dump(logs[-300:], f, indent=2)

        print(f"[GhostBuild] Code saved to: {full_path}")

        if inject:
            inject_generated_code(code, module_name=filename.replace(".py", ""))
            print(f"[GhostBuild] Code injected successfully.")

        return full_path

    except Exception as e:
        print(f"[GhostBuild Error] Failed to write or inject code: {e}")
        return None