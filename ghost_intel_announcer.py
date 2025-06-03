# === FILE: ghost_intel_announcer.py ===
# 📢 Ghost Intel Announcer – Narrates the Ghost Intel Feed updates

import os
from datetime import datetime
from gpt_voice_bridge import speak_gpt_response
from voice_engine import speak_text
from ghost_queries import generate_ghost_intel

def announce_ghost_intel_as_file(results):
    """
    Converts the latest Ghost Intel into a narrated audio report and saves as a voice file.

    Args:
        results (list): List of dicts from ghost_queries.py

    Returns:
        dict: Voice file path and log entry
    """
    try:
        print("[GHOST ANNOUNCER] 🔊 Generating spoken intel summary...")

        lines = []
        for idx, item in enumerate(results, start=1):
            if "error" in item:
                lines.append(f"Error: {item['error']}")
                continue

            lines.append(
                f"Report {idx}: {item['title']}. "
                f"Summary: {item['summary']}. Source: {item['source']}."
            )

        text_to_speak = "\n".join(lines)
        voice_path = speak_gpt_response(text_to_speak)

        log_path = log_intel_announcement(text_to_speak, voice_path)
        return {"status": "spoken", "audio": voice_path, "log": log_path}

    except Exception as e:
        print(f"[GHOST ANNOUNCER ERROR] ❌ {e}")
        return {"status": "error", "message": str(e)}


def announce_ghost_intel_live(topics):
    """
    Pulls intel and speaks it aloud using the voice engine in real time.

    Args:
        topics (list): List of topic strings to pull reports for.

    Returns:
        list: The full intel result list
    """
    print("[INTEL ANNOUNCER] 🔊 Generating intel for live announcement...")
    results = generate_ghost_intel(topics)

    for item in results:
        if "error" in item:
            speak_text(f"Error fetching data for {item.get('topic', 'unknown')}: {item['error']}")
            continue

        message = f"📢 {item['title']}. Source: {item['source']}. Summary: {item['summary']}"
        speak_text(message)

    return results


def log_intel_announcement(text, audio_path):
    os.makedirs("logs/ghost_intel", exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = f"logs/ghost_intel/intel_{timestamp}.log"
    
    with open(log_file, "w", encoding="utf-8") as log:
        log.write(f"[{timestamp} UTC] GHOST INTEL REPORT\n{text}\nMP3: {audio_path}\n")
    
    return log_file