# === FILE: macro_generator.py ===

# 🔁 Macro Generator – Builds reusable trading macros or task chains

def generate_macro(task):
    print(f"[MacroGen] 🔁 Creating macro for: {task}")
    return f"# Macro for {task}\ndef run():\n    print('Running {task}')\n"