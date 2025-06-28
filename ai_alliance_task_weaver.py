# === FILE: alliance_task_weaver.py ===
# 🧵 Alliance Task Weaver – Enables joint code authoring and macro generation across AIs and PTM bots

import os
import json
import datetime
from utils.logger import log_event
from utils.file_utils import save_file

class AllianceTaskWeaver:
    def __init__(self, working_dir="weaver_tasks"):
        self.working_dir = working_dir
        os.makedirs(self.working_dir, exist_ok=True)
        print("[TaskWeaver] 🧵 Alliance Task Weaver initialized.")

    def create_task(self, title, description,