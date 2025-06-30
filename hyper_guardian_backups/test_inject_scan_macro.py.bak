# === FILE: test_inject_scan_macro.py ===
from gpt_code_dispatcher import dispatch_code

scan_macro_code = '''
import os
import re

PROJECT_ROOT = "."
LOG_FILE = "function_log.txt"

def scan_functions():
    functions_found = []

    for root, dirs, files in os.walk(PROJECT_ROOT):
        for file in files:
            if file.endswith(".py") and file != os.path.basename(__file__):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        for i, line in enumerate(lines):
                            match = re.match(r'\\s*def\\s+([a-zA-Z_][a-zA-Z0-9_]*)\\s*\