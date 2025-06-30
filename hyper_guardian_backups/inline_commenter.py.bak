# === FILE: inline_commenter.py ===
"""
Inline Commenter:
Reads Python strategy code and injects contextual inline comments
for improvements, warnings, or suggestions from the reviewing assistant.
"""

import os
import re
from datetime import datetime

# === Config ===
COMMENT_TAG = "# 💬"
COMMENT_LIBRARY = {
    "price <": "Consider lowering threshold for high-volatility stocks",
    "price >": "Might be too aggressive on exit — confirm with RSI",
    "return \"Buy": "Add volume filter for better confidence",
    "return \"Sell": "Maybe check for MACD confirmation first"
}
COMMENTED_DIR = "data/strategy_comments"
os.makedirs(COMMENTED_DIR, exist_ok=True)

# === Core Function ===
def inject_inline_comments(file_path, reviewer="PTM"):
    """
    Adds inline comments to code based on pattern matching.
    Uses fixed comment library + dynamic suggestions for thresholds and constants.
    """
    if not os.path.exists(file_path):
        print(f"[Inline Commenter] ❌ File not found: {file_path}")
        return None

    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"[Inline Commenter] ❌ Read error: {e}")
        return None

    reviewed_lines = []
    inserted = False

    for line in lines:
        reviewed_lines.append(line)
        stripped = line.strip()

        # === Static comment matches
        for keyword, comment in COMMENT_LIBRARY.items():
            if keyword in stripped:
                reviewed_lines.append(f"{COMMENT_TAG} Suggested by {reviewer}: {comment}\n")
                inserted = True
                break

        # === Soft pattern for numeric values
        if re.search(r"\s=\s\d+", stripped) and not stripped.startswith("#"):
            reviewed_lines.append(f"{COMMENT_TAG} {reviewer} TIP: Consider externalizing this value for tuning.\n")
            inserted = True

    if not inserted:
        print("[Inline Commenter] ⚠️ No patterns found to comment on.")
        return None

    # Save with timestamp + directory
    base = os.path.basename(file_path).replace(".py", "")
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    new_filename = f"{reviewer}_{base}_COMMENTED_{timestamp}.py"
    new_path = os.path.join(COMMENTED_DIR, new_filename)

    try:
        with open(new_path, "w") as f:
            f.writelines(reviewed_lines)
        print(f"[💬 Inline Feedback] File saved: {new_filename}")
        return new_path
    except Exception as e:
        print(f"[Inline Commenter] ❌ Write error: {e}")
        return None