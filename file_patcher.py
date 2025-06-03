# === FILE: file_patcher.py ===
# 🩹 PTM File Patcher – Overwrites broken files with AI-generated fixed code

import os

def patch_file(file_path, new_code):
    """
    Overwrites the target file with AI-generated fixed code.

    Args:
        file_path (str): Path to the file to patch.
        new_code (str): The corrected Python code to write.

    Returns:
        dict: Result status and file path or error message.
    """
    try:
        if not file_path or not new_code:
            raise ValueError("File path or code is missing.")

        # Ensure parent directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Write the new fixed code to the file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_code)

        print(f"[PATCH] ✅ File patched successfully: {file_path}")
        return {"status": "success", "file": file_path}

    except FileNotFoundError:
        print(f"[PATCH ERROR] ❌ Target file not found: {file_path}")
        return {"status": "error", "message": "File not found.", "file": file_path}

    except Exception as e:
        print(f"[PATCH ERROR] ❌ Could not patch file: {e}")
        return {"status": "error", "file": file_path, "message": str(e)}