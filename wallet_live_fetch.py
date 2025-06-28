# === FILE: wallet_live_fetch.py ===

from flask import Blueprint, request, jsonify
from web3 import Web3

wallet_live_fetch = Blueprint('wallet_live_fetch', __name__)

INFURA_URL = "https://mainnet.infura.io/v3/04d5c08731431f82124b8c6bdab28f"
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

@wallet_live_fetch.route("/get_balance", methods=["POST"])
def get_balance():
    try:
        data = request.get_json()
        address = data.get("address")

        if not web3.isAddress(address):
            return jsonify({"error": "Invalid Ethereum address"}), 400

        balance_wei = web3.eth.get_balance(address)
        balance_eth = web3.fromWei(balance_wei, 'ether')

        return jsonify({
            "address": address,
            "balance": f"{balance_eth:.6f} ETH",
            "status": "✅ Live"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500