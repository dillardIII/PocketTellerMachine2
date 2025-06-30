from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import time
from datetime import datetime
from cole_voice_summary_generator import generate_voice_summaries
from cole_voice_narrator import generate_voice_mp3

# === Config ===
VOICE_SUMMARY_FILE = "data/trade_voice_summary.json"
NARRATION_LOG_FILE = "data/voice_narration_log.json"
NARRATED_DIR = "data/voice_summaries/"
LOOP_SECONDS = 180  # Check every 3 minutes

# === Ensure output directory exists ===
os.makedirs(NARRATED_DIR, exist_ok=True)

# === Load summaries ===
def load_voice_summaries():
    if not os.path.exists(VOICE_SUMMARY_FILE):
        return []
    with open(VOICE_SUMMARY_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# === Get already narrated summaries by ID ===
def get_already_narrated_ids():
    if not os.path.exists(NARRATION_LOG_FILE):
        return []
    with open(NARRATION_LOG_FILE, "r") as f:
        try:
            logs = json.load(f)
            return [log["summary_id"] for log in logs]
        except json.JSONDecodeError:
            return []

# === Log narration ===
def log_narration(summary_id):
    logs = []
    if os.path.exists(NARRATION_LOG_FILE):
        try:
            with open(NARRATION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []
    logs.append({"summary_id": summary_id, "timestamp": datetime.now().isoformat()})
    with open(NARRATION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Simulate or generate real narration ===
def simulate_or_generate_narration(summary):
    summary_id = summary.get("id", "")
    text = summary.get("summary", "")
    output_filename = f"{summary_id}.mp3"
    output_path = os.path.join(NARRATED_DIR, output_filename)

    if not os.path.exists(output_path):
        try:
            # Replace with generate_voice_mp3(text, output_path) for real voice generation
            generate_voice_mp3(text, output_path)
            print(f"[NARRATOR]: Generated MP3 voice summary at {output_path}")
        except Exception as e:
            print(f"[NARRATOR]: Fallback simulation due to error: {e}")
            with open(output_path.replace(".mp3", ".txt"), "w") as f:
                f.write(f"[Narrated]: {text}")
            print(f"[NARRATOR]: Simulated narration saved as TXT at {output_path.replace('.mp3', '.txt')}")

# === Main Daemon Loop ===
def narrator_loop():
    print("[NARRATOR DAEMON]: Voice Narrator Daemon running...")
    while True:
        try:
            summaries = load_voice_summaries()
            already_narrated = get_already_narrated_ids()
            new_summaries = [s for s in summaries if s.get("id") not in already_narrated]

            if new_summaries:
                for summary in new_summaries:
                    simulate_or_generate_narration(summary)
                    log_narration(summary.get("id"))
                print(f"[NARRATOR DAEMON]: Narrated {len(new_summaries)} new summaries.")
            else:
                print("[NARRATOR DAEMON]: No new summaries to narrate.")
        except Exception as e:
            print(f"[NARRATOR DAEMON ERROR]: {e}")

        time.sleep(LOOP_SECONDS)

# === Run Daemon ===
if __name__ == "__main__":
    # === Real Narrator Loop ===
    narrator_loop()

    # === Simulated Fallback Loop (uncomment if needed) ===
    # while True:
    #     print("[Daemon]: Voice Narrator Daemon active... (simulated)")
    #     # Narrate or summarize events
    #     time.sleep(60)