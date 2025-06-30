# 📄 Vault Document Viewer – Displays PDF and TXT documents stored in the vault

import os
import time
import fitz  # PyMuPDF
from utils.logger import log_event

DOCUMENT_DIR = "vault/docs/"
POLL_INTERVAL = 20  # seconds

def display_text_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            print(f"\n📄 [Document: {os.path.basename(file_path)}]\n")
            print(content[:500] + "\n...\n" if len(content) > 500 else content)
        log_event("DocViewer", {"displayed": file_path})
    except Exception as e:
        log_event("DocViewer", {"error": f"Text read failed: {str(e)}"})

def display_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        print(f"\n📘 [PDF: {os.path.basename(file_path)}]\n")
        for page in doc:
            text = page.get_text()
            print(text[:500] + "\n...\n" if len(text) > 500 else text)
            break  # Display only the first page
        doc.close()
        log_event("DocViewer", {"displayed": file_path})
    except Exception as e:
        log_event("DocViewer", {"error": f"PDF read failed: {str(e)}"})

def scan_document_folder():
    seen = set()
    log_event("DocViewer", {"status": "📚 Watching for new document files..."})

    while True:
        try:
            for f in os.listdir(DOCUMENT_DIR):
                full_path = os.path.join(DOCUMENT_DIR, f)
                if f not in seen and os.path.isfile(full_path):
                    seen.add(f)
                    if f.endswith(".txt"):
                        display_text_file(full_path)
                    elif f.endswith(".pdf"):
                        display_pdf(full_path)
        except Exception as e:
            log_event("DocViewer", {"error": f"Folder scan error: {str(e)}"})

        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    scan_document_folder()