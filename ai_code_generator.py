# === FILE: ai_code_generator.py ===

import os
import openai
import requests

# === API Keys from Environment ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REPLIT_API_KEY = os.getenv("REPLIT_AI_KEY")

if not OPENAI_API_KEY:
    raise ValueError("🛑 Missing OPENAI_API_KEY in environment variables.")

openai.api_key = OPENAI_API_KEY

# === Prompt Template for Traceback-Based Fixing ===
FIX_PROMPT_TEMPLATE = """
You are a code repair AI. A Python file has a bug. Your job is to fix it based on the following error and traceback.

--- ERROR DETAILS ---
File: {file}
Error: {error}

--- TRACEBACK ---
{traceback}

Now return ONLY the corrected version of the entire file in valid Python code. Do not return explanations.
"""

# === Generate Fix Using GPT (Traceback Style) ===
def generate_code_fix(error_info):
    if not error_info or not error_info.get("error") and not error_info.get("error_message"):
        return None

    try:
        prompt = FIX_PROMPT_TEMPLATE.format(
            file=error_info.get("file", "unknown"),
            error=error_info.get("error_message") or error_info.get("error"),
            traceback=error_info.get("traceback", "")
        )

        print("[AI Generator] Sending error info to GPT for fix...")

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional Python code repair agent."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            max_tokens=1200
        )

        fix_code = response["choices"][0]["message"]["content"].strip()

        print("[AI Generator] Fix generated successfully.")
        return fix_code

    except Exception as e:
        print(f"[AI Generator] Failed to generate fix: {e}")
        return None

# === Generate Code Fix using Replit AI ===
def generate_code_fix_replit(file_path, broken_code, error_msg):
    if not REPLIT_API_KEY:
        print("[Replit Code Generator] Missing REPLIT_AI_KEY.")
        return None

    prompt = f"""
You are an expert Python developer.
A bug has been detected in file: {file_path}

Error message:
{error_msg}

Code snippet with the issue:
{broken_code}

Please provide a fixed and corrected version of the code snippet.
Only return valid Python code.
"""

    headers = {"Authorization": f"Bearer {REPLIT_API_KEY}"}
    data = {"prompt": prompt, "max_tokens": 600}

    try:
        response = requests.post("https://api.replit.com/v0/codegen", headers=headers, json=data)
        result = response.json()
        return result.get("completion", "").strip()
    except Exception as e:
        print(f"[Replit Code Generator] API call failed: {e}")
        return None
