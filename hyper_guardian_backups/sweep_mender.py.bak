# === FILE: sweep_mender.py ===

# 🧹 Sweep Mender – Runs behind SweepHandler and fixes light file issues

def mend_file_if_needed(filepath):
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
        if not lines or not lines[0].startswith("#"):
            lines.insert(0, "# Autopatched by SweepMender\n")
            with open(filepath, 'w') as f:
                f.writelines(lines)
            print(f"[SweepMender] 🩹 Patched: {filepath}")
    except Exception as e:
        print(f"[SweepMender] ⚠️ Could not mend: {filepath}")