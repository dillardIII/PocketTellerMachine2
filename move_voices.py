from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import shutil

# === Source folder where uploaded files are ===
source_folder = "/mnt/data"

# === Target folder where voice previews are served from ===
target_folder = "static/audio"
os.makedirs(target_folder, exist_ok=True)

# === Rename map for Replit uploaded IDs (legacy support) ===
legacy_map = {
    "file-HLaWA2DkWAngUVhF2Z2T8V": "mentor.mp3",
    "file-Cd6kTRj5HZJJC1hnRYFXHr": "mo_cash.mp3",
    "file-69YCoPQZynkoWktT5itQAc": "drill_instructor.mp3",
    "file-AiSoXG64V8eSpEF9ymuP35": "comedian.mp3",
    "file-KPZNxfzcD5XGeqsV9vD3LZ": "malik.mp3"
}

# === Rename map for preview-named MP3s ===
preview_map = {
    "mentor_preview.mp3": "mentor.mp3",
    "mo_cash_preview.mp3": "mo_cash.mp3",
    "drill_instructor_preview.mp3": "drill_instructor.mp3",
    "comedian_preview.mp3": "comedian.mp3",
    "shadow_preview.mp3": "shadow.mp3",
    "og_preview.mp3": "the_og.mp3",
    "malik_preview.mp3": "malik.mp3",
    "strategist_preview.mp3": "strategist.mp3",
    "optimist_preview.mp3": "the_optimist.mp3",
    "chill_trader_preview.mp3": "the_chill_trader.mp3"
}

# === Combine both maps ===
rename_map = {**legacy_map, **preview_map}

# === Move and rename ===
for original, new_name in rename_map.items():
    src = os.path.join(source_folder, original)
    dst = os.path.join(target_folder, new_name)
    if os.path.exists(src):
        shutil.copyfile(src, dst)
        print(f"Moved: {original} → {new_name}")
    else:
        print(f"Missing: {original}")

def log_event():ef drop_files_to_bridge():