from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import openai
import json
import uuid
import subprocess
import requests
from datetime import datetime
from resume_tasks import log_task

# === Config ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
COLE_VOICE_ID = os.getenv("COLE_VOICE_ID") or "EXAVITQu4vr4xnSDxMaL"
BASE_DIR = "modules"
STRATEGY_FILE = "data/option_strategies.json"
LOG_FILE = "data/ghost_writer_log.json"

openai.api_key = OPENAI_API_KEY


# === Task Parser ===
def parse_task(description):
    return {
        "prompt": f"Write a Python module that does the following:\n{description}\n\nInclude detailed comments in the code.",
        "filename": f"{uuid.uuid4().hex[:8]}.py"
    }


# === Code Generator ===
def generate_code(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
            max_tokens=1200
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"# ERROR: {e}"


# === Validator ===
def validate_code(code):
    try:
        compile(code, "<string>", "exec")
        return True
    except Exception as e:
        print(f"Code validation failed: {e}")
        return False


# === Save Code to File ===
def save_code(code, filename, folder="generated"):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(code)
    return path


# === Execute Code and Capture Output ===
def run_module(path):
    try:
        result = subprocess.run(["python3", path], capture_output=True, text=True, timeout=10)
        output = result.stdout.strip()
        error = result.stderr.strip()
        return output, error
    except Exception as e:
        return "", f"Execution error: {e}"


# === Logger ===
def log_ghost_action(task_desc, filename, code, output, error):
    log_entry = {
        "id": uuid.uuid4().hex,
        "task": task_desc,
        "filename": filename,
        "timestamp": str(datetime.now()),
        "code_preview": code[:200] + "...",
        "execution_output": output,
        "execution_error": error,
        "favorite": False  # NEW
    }
    os.makedirs("data", exist_ok=True)
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE) as f:
            logs = json.load(f)
    logs.append(log_entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)


# === Feedback Generator ===
def generate_cole_feedback(filename, output, error):
    if error:
        return f"Module {filename} ran into an issue. Here’s what came back:\n{error}"
    elif output:
        return f"Module {filename} executed cleanly. Output:\n{output}"
    else:
        return f"Module {filename} ran successfully, but no output was returned."


# === ElevenLabs Voice (Mood-Aware) ===
def speak_as_cole(message_text, filename="cole_feedback.mp3", mood="neutral"):
    try:
        if not ELEVENLABS_API_KEY:
            raise ValueError("ELEVENLABS_API_KEY not set in environment.")

        url = f"https://api.elevenlabs.io/v1/text-to-speech/{COLE_VOICE_ID}"
        headers = {
            "xi-api-key": ELEVENLABS_API_KEY,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg"
        }

        # === Mood-to-Voice Settings Mapping ===
        voice_settings = {
            "neutral": {"stability": 0.5, "similarity_boost": 0.75},
            "excited": {"stability": 0.3, "similarity_boost": 0.9},
            "calm":    {"stability": 0.6, "similarity_boost": 0.65},
            "disappointed": {"stability": 0.8, "similarity_boost": 0.4}
        }

        payload = {
            "text": message_text,
            "voice_settings": voice_settings.get(mood, voice_settings["neutral"])
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            path = os.path.join("static", "audio", filename)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "wb") as f:
                f.write(response.content)
            return path
        else:
            print("ElevenLabs Error:", response.text)
            return None
    except Exception as e:
        print("Cole voice generation error:", e)
        return None


# === Master Function: Prompt > Code > Run > Save > Speak ===
def write_module(task_description):
    if not OPENAI_API_KEY:
        return {
            "status": "fail",
            "message": "OPENAI_API_KEY not set.",
            "assistant_feedback": "I can't reach the code lab right now.",
            "voice_file": None
        }

    task = parse_task(task_description)
    code = generate_code(task['prompt'])

    if not validate_code(code):
        return {
            "status": "fail",
            "message": "Code validation failed.",
            "assistant_feedback": "Syntax did not align with the flow. I'll trace it again when you're ready.",
            "voice_file": None
        }

    # Save full module in /modules/coda/
    coda_folder = os.path.join(BASE_DIR, "coda")
    os.makedirs(coda_folder, exist_ok=True)
    filepath = os.path.join(coda_folder, task['filename'])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)

    # Execute code for output
    output, error = run_module(filepath)

    # Log it
    log_ghost_action(task_description, task['filename'], code, output, error)

    # Save as a strategy too
    strategy_name = f"strategy_{uuid.uuid4().hex[:6]}"
    strategy_entry = {
        "id": strategy_name,
        "description": task_description,
        "code": code,
        "created_at": datetime.now().isoformat()
    }

    try:
        with open(STRATEGY_FILE, "r") as f:
            strategies = json.load(f)
    except FileNotFoundError:
        strategies = []

    strategies.append(strategy_entry)
    with open(STRATEGY_FILE, "w") as f:
        json.dump(strategies, f, indent=2)

    # Task memory
    log_task(task_description, code, status="completed")

    # Voice feedback
    cole_message = generate_cole_feedback(task['filename'], output, error)
    voice_filename = f"cole_feedback_{task['filename'].replace('.py', '')}.mp3"
    voice_path = speak_as_cole(cole_message, voice_filename)

    print(f"New module saved to: {filepath}")
    return {
        "status": "success",
        "strategy_name": strategy_name,
        "file": filepath,
        "output": output,
        "error": error,
        "assistant_feedback": cole_message,
        "voice_file": voice_path
    }

def log_event():ef drop_files_to_bridge():