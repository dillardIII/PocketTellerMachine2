# === FILE: diff_viewer.py ===
# Code Diff Viewer – Highlights changes between old and new code

import difflib

def generate_diff_html(before_code: str, after_code: str, file_name="file.py") -> str:
    differ = difflib.HtmlDiff(wrapcolumn=80)
    diff_html = differ.make_file(
        before_code.splitlines(), 
        after_code.splitlines(), 
        fromdesc=f"Before: {file_name}", 
        todesc=f"After: {file_name}"
    )
    return diff_html

def save_diff_report(before_code: str, after_code: str, file_name: str) -> str:
    html = generate_diff_html(before_code, after_code, file_name)
    output_path = f"logs/diffs/{file_name.replace('/', '_')}_diff.html"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    return output_path