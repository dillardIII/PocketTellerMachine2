from ghost_env import INFURA_KEY, VAULT_ADDRESS
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

SCOPES = ['https://www.googleapis.com/auth/drive']

flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
creds = flow.run_local_server(port=8081)

with open("token.pkl", "wb") as token:
    pickle.dump(creds, token)

print("Google OAuth Complete.")

def log_event():ef drop_files_to_bridge():