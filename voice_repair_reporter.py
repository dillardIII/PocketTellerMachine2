# === FILE: voice_repair_reporter.py ===
# 🎤 PTM Voice Repair Reporter – Narrates repair actions

import os
import datetime
from datetime import datetime as dt

# Optional: GPT voice system if present
try:
    from gpt_voice_bridge import speak_gpt_response
except ImportError:
    speak_gpt_response = None

# === 📢 PRIMARY GPT-BASED VOICE SYSTEM ===
def generate_voice_report(file, summary, result):
    spoken_summary = f"PTM just patched {file}. The change was: {summary}. Result: {result}."
    print(f"[🎤 Voice Report] {spoken_summary}")

    if speak_gpt_response:
        try:
            voice_path = speak_gpt_response(spoken_summary)
            log_voice_event(file, spoken_summary, voice_path)
            return {"status": "spoken", "file": file, "audio": voice_path}
        except Exception as e:
            print(f"[Voice Reporter ERROR] {str(e)}")
            return {"status": "error", "message": str(e)}
    else:
        print("[VoiceReport] ⚠️ GPT voice system not loaded. Defaulting to console.")
        log_voice_event(file, spoken_summary, "console_only")
        return {"status": "console", "file": file}

# === 📜 LOGGING ===
def log_voice_event(file, text, path):
    os.makedirs("logs", exist_ok=True)
    with open("logs/voice_repair.log", "a") as log:
        log.write(f"\n[{dt.utcnow()}] {file}\n{text}\nMP3: {path}\n")

# === 🧠 FALLBACK: TTS FOR NON-GPT MODE OR DEBUGGING ===
def text_to_speech(text, output_path):
    try:
        from gtts import gTTS
        tts = gTTS(text)
        tts.save(output_path)
        print(f"[VOICE] 🎧 Voice report saved to {output_path}")
    except Exception as e:
        print(f"[VOICE ERROR] Could not generate voice: {e}")

def fallback_generate_voice_report(file_path, context, deploy_result):
    try:
        timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = os.path.basename(file_path)
        summary = (
            f"Repair Report. File: {file_name}. "
            f"Context: {context}. "
            f"Deploy result: {deploy_result}."
        )

        output_dir = "voice_reports"
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"{file_name}_{timestamp}.mp3")

        text_to_speech(summary, output_file)
    except Exception as e:
        print(f"[VOICE REPORT ERROR] ❌ {e}")

# === 🗣️ LIGHTWEIGHT CONSOLE-ONLY FOR BASIC RUNS ===
def simple_console_voice_report(file_path, context, deploy_status):
    print(f"[VoiceReport] 🎙️ {context} on {file_path} – Status: {deploy_status}")