# === FILE: cole_tools/strategy_writer.py ===

import os
from datetime import datetime

def write_strategy_note(note_text):
    """
    Saves the provided strategy note text to a timestamped file.
    """
    os.makedirs("data", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"data/strategy_note_{timestamp}.txt"

    with open(file_path, "w") as f:
        f.write(note_text)

    return file_path