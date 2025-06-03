# === FILE: syntax_fixer.py ===
# Attempts to auto-correct common syntax issues in Python code

import ast
import re

def auto_fix_syntax(code):
    """
    Fixes common syntax errors in Python code.
    Returns cleaned version of the code.
    """

    fixed = code

    # === Fix #1: Common mistaken assignment in conditionals ===
    fixed = re.sub(r"if\s+(.*?)\s+=\s+(.*?):", r"if \1 == \2:", fixed)

    # === Fix #2: Missing colons at end of control statements ===
    fixed = re.sub(r"(?<!:)\n(\s*)(if|for|while|def|class)\b(.*)(?<!:)\n", r"\1\2\3:\n", fixed)

    # === Fix #3: Replace tabs with 4 spaces ===
    fixed = fixed.replace("\t", "    ")

    # === Fix #4: Ensure consistent quote usage ===
    fixed = re.sub(r'[“”]', '"', fixed)
    fixed = re.sub(r"[‘’]", "'", fixed)

    # === Fix #5: Remove duplicated imports ===
    lines = fixed.split("\n")
    seen = set()
    cleaned = []
    for line in lines:
        if line.strip().startswith("import") or line.strip().startswith("from"):
            if line.strip() in seen:
                continue
            seen.add(line.strip())
        cleaned.append(line)

    # === Fix #6: Remove trailing whitespace ===
    fixed = "\n".join([line.rstrip() for line in cleaned])

    return fixed