from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: voice_transfer_engine.py ===
# 🎙️ Voice Transfer Engine – Accepts voice-triggered ETH transfers from Vault Wallet

from flask import Blueprint, request, jsonify
from web3 import Web3
import os
from eth_account import Account
from dotenv import load_dotenv

load_dotenv()

voice_transfer_engine = Blueprint('voice_transfer_engine', __name__)

# === ENV CONFIG ===
INFURA_API_KEY = os.getenv("INFURA_API_KEY")
VAULT_KEY = os.getenv("METAMASK_VAULT_KEY")
VAULT_ADDRESS = os.getenv("METAMASK_VAULT_ADDRESS")

# === Web3 Setup ===
provider_url = f"https://mainnet.infura.io/v3/{INFURA_API_KEY}"
w3 = Web3(Web3.HTTPProvider(provider_url))

@voice_transfer_engine.route("/voice_send_eth", methods=["POST"])
def voice_send_eth():
    try:
        data = request.get_json()
        to_address = data.get("to_address")
        amount_eth = data.get("amount_eth")
        pin = data.get("pin")

        if not all([to_address, amount_eth, pin]):
            return jsonify({"error": "Missing required fields"}), 400

        if pin != "1234":  # 🔐 Replace this PIN check with secure vault auth in future:
            return jsonify({"error": "Invalid transfer PIN"}), 403

        amount_wei = w3.to_wei(float(amount_eth), "ether")
        nonce = w3.eth.get_transaction_count(VAULT_ADDRESS)

        gas_price = w3.eth.gas_price
        tx = {
            "nonce": nonce,
            "to": to_address,
            "value": amount_wei,
            "gas": 21000,
            "gasPrice": gas_price,
        }

        signed_tx = w3.eth.account.sign_transaction(tx, VAULT_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

        return jsonify({
            "status": "success",
            "tx_hash": tx_hash.hex()
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

def log_event():ef drop_files_to_bridge():