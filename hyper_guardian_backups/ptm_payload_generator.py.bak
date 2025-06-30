import os

def list_current_modules():
    module_dir = "."  # base scan directory
    modules = []

    for root, dirs, files in os.walk(module_dir):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, module_dir)
                modules.append(rel_path)

    return modules

if __name__ == "__main__":
    for m in list_current_modules():
        print(f"[Payload] ✅ Found module: {m}")