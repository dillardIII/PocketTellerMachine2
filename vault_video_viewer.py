from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 📹 Vault Video Viewer – Auto-plays new video files added to the vault

import os
import time
import cv2
from utils.logger import log_event

VIDEO_DIR = "vault/video/"
SUPPORTED_FORMATS = [".mp4", ".avi", ".mov"]
POLL_INTERVAL = 20  # seconds

def play_video(file_path):
    try:
        cap = cv2.VideoCapture(file_path)

        if not cap.isOpened():
            log_event("VideoViewer", {"error": f"Failed to open: {file_path}"})
            return

        print(f"\n🎥 [Playing: {os.path.basename(file_path)}]")
        log_event("VideoViewer", {"played": file_path})

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Vault Video Viewer', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        log_event("VideoViewer", {"error": str(e)})

def scan_video_folder():
    seen = set()
    log_event("VideoViewer", {"status": "📺 Watching for new video logs..."})

    while True:
        try:
            for f in os.listdir(VIDEO_DIR):
                full_path = os.path.join(VIDEO_DIR, f)
                if f not in seen and os.path.isfile(full_path):
                    if any(f.endswith(ext) for ext in SUPPORTED_FORMATS):
                        seen.add(f)
                        play_video(full_path)
        except Exception as e:
            log_event("VideoViewer", {"error": f"Video scan error: {str(e)}"})

        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    scan_video_folder()