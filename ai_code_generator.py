import os
import openai
import requests

# === API Keys from Environment ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REPLIT_API_KEY = os.getenv("REPLIT_AI_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY in environment variables.")

openai.api_key = OPENAI_API_KEY

# === Generate Code Fix using Replit AI ===
def generate_code_fix_replit(file_path, broken_code, error_msg):
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

# === Generate Code Fix using OpenAI GPT-4 ===
def generate_code_fix(error_data):
    if not error_data or not error_data.get("error"):
        return None

    prompt = f"""You are an AI programmer. The following Python file encountered an error:
---
File: {error_data['file']}
Line: {error_data.get('line', '?')}
Error:
{error_data['error']}
---

Please return a complete corrected version of the file with this issue fixed.
ONLY return working Python code. No explanations. No markdown formatting.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert Python developer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1200
        )

        fix = response.choices[0].message.content.strip()
        print(f"[OpenAI Code Generator] Suggested Fix:\n{fix}")
        return fix

    except Exception as e:
        print(f"[OpenAI Code Generator] Error generating fix: {e}")
        return None