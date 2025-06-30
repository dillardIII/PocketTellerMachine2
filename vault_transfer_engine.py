from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: vault_transfer_engine.py ===
from flask import Blueprint, request, jsonify
from web3 import Web3
import os

vault_transfer_engine = Blueprint('vault_transfer_engine', __name__)

INFURA_URL = f"https://mainnet.infura.io/v3/{os.getenv('INFURA_API_KEY')}"
VAULT_PRIVATE_KEY = os.getenv("METAMASK_VAULT_KEY")
VAULT_ADDRESS = os.getenv("METAMASK_VAULT_ADDRESS")

web3 = Web3(Web3.HTTPProvider(INFURA_URL))

@vault_transfer_engine.route('/send_eth', methods=['POST'])
def send_eth():
    try:
        data = request.json
        to_address = data.get("to")
        amount_eth = float(data.get("amount", 0))

        # Validation
        if not web3.isAddress(to_address):
            return jsonify({"error": "Invalid receiving address"}), 400
        if amount_eth <= 0:
            return jsonify({"error": "Amount must be greater than 0"}), 400
        if not VAULT_PRIVATE_KEY or not VAULT_ADDRESS:
            return jsonify({"error": "Vault credentials missing"}), 500

        # Convert ETH to Wei
        amount_wei = web3.toWei(amount_eth, 'ether')

        # Nonce + transaction details
        nonce = web3.eth.getTransactionCount(VAULT_ADDRESS)
        tx = {
            'nonce': nonce,
            'to': to_address,
            'value': amount_wei,
            'gas': 21000,
            'gasPrice': web3.eth.gas_price,
        }

        # Sign and send
        signed_tx = web3.eth.account.sign_transaction(tx, private_key=VAULT_PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        return jsonify({
            "status": "Success",
            "tx_hash": web3.toHex(tx_hash)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():