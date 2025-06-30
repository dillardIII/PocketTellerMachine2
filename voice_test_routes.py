from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: voice_test_routes.py ===
# 🎛️ Voice Test Routes – Web triggers for testing wallet summary voice tools

from flask import Blueprint
from wallet_voice_generator import speak_wallet_summary
from wallet_voice_summary import play_wallet_summary

voice_test_routes = Blueprint("voice_test_routes", __name__)

@voice_test_routes.route("/wallet_summary_live", methods=["GET"])
def trigger_summary_gen():
    return speak_wallet_summary()

@voice_test_routes.route("/wallet_summary_voice", methods=["GET"])
def trigger_summary_play():
    return play_wallet_summary()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():