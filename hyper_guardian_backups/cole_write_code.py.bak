#=== FILE: cole_write_code.py ===

def cole_write_code(task): import os os.makedirs("cole_generated_code", exist_ok=True) description = task.get("description", "default_task") filename = task.get("filename", "auto_generated_task.py") code = f"""# Auto-generated code\nprint("Running task: {description}")\n""" with open(f"cole_generated_code/{filename}", "w") as f: f.write(code) print(f"[Code Writer] Wrote: {filename}")

