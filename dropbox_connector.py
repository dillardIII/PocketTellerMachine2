from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: dropbox_connector.py ===
import dropbox
import os

DROPBOX_TOKEN = os.getenv("DROPBOX_ACCESS_TOKEN")
dbx = dropbox.Dropbox(DROPBOX_TOKEN)

def upload_to_dropbox(local_path, dropbox_path):
    with open(local_path, "rb") as f:
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))
    print(f"[Dropbox] Uploaded {local_path} to {dropbox_path}")

def download_from_dropbox(dropbox_path, local_path):
    metadata, res = dbx.files_download(dropbox_path)
    with open(local_path, "wb") as f:
        f.write(res.content)
    print(f"[Dropbox] Downloaded {dropbox_path} to {local_path}")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():