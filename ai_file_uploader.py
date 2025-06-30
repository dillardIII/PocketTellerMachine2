from ghost_env import INFURA_KEY, VAULT_ADDRESS
import requests

def upload_to_ptm(file_path):
    url = "http://localhost:5000/upload"  # Or replace with Replit URL if deployed:
    with open(file_path, 'rb') as f:
        files = {'file': (file_path, f)}
        response = requests.post(url, files=files)
        return response.json()

# Example Usage
if __name__ == "__main__":
    result = upload_to_ptm("ghostbuild_voice.html")
    print(result)

def log_event():ef drop_files_to_bridge():