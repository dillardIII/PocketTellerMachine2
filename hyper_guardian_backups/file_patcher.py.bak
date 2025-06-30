# === FILE: file_patcher.py ===
# 🩹 File Patcher – Safely overwrites or patches code files

def patch_file(file_path, new_code):
    try:
        with open(file_path, "w") as f:
            f.write(new_code)
        print(f"[Patcher] ✅ Patched {file_path}")
        return {"status": "success", "file": file_path}
    except Exception as e:
        print(f"[Patcher] ❌ Failed patching {file_path}: {e}")
        return {"status": "error", "message": str(e)}