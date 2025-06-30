from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: wallet_env_fetch.py ===
from flask import Blueprint, jsonify
from web3 import Web3
import os

wallet_env_fetch = Blueprint('wallet_env_fetch', __name__)

INFURA_URL = f"https://mainnet.infura.io/v3/{os.getenv('INFURA_API_KEY')}"
ADDRESS = os.getenv("METAMASK_WALLET_ADDRESS")

web3 = Web3(Web3.HTTPProvider(INFURA_URL))

@wallet_env_fetch.route("/wallet_balance_env", methods=["GET"])
def get_balance_from_env():
    try:
        if not web3.isConnected():
            return jsonify({"error": "Web3 connection failed"}), 500

        if not ADDRESS:
            return jsonify({"error": "Wallet address not set"}), 400

        balance_wei = web3.eth.get_balance(ADDRESS)
        balance_eth = web3.fromWei(balance_wei, "ether")

        return jsonify({
            "address": ADDRESS,
            "balance_eth": str(balance_eth),
            "status": "Live"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():