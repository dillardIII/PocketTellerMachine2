from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: wallet_api_routes.py ===
# 📡 PTM Wallet API Routes – JSON access to live wallet and token data

from flask import Blueprint, jsonify, request
from wallet_manager import WalletManager

wallet_api_routes = Blueprint("wallet_api_routes", __name__)
manager = WalletManager()

# === Get all wallet data ===
@wallet_api_routes.route("/api/wallet", methods=["GET"])
def get_wallet():
    data = manager.load_wallet()
    return jsonify(data), 200

# === Update single asset ===
@wallet_api_routes.route("/api/wallet/update", methods=["POST"])
def update_wallet():
    try:
        payload = request.get_json()
        asset = payload.get("asset")
        amount = payload.get("amount")

        if not asset or amount is None:
            return jsonify({"error": "Missing asset or amount"}), 400

        manager.update_asset(asset, amount)
        return jsonify({
            "status": "updated",
            "asset": asset,
            "amount": amount
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# === Delete asset ===
@wallet_api_routes.route("/api/wallet/delete", methods=["POST"])
def delete_wallet_asset():
    try:
        payload = request.get_json()
        asset = payload.get("asset")

        if not asset:
            return jsonify({"error": "Missing asset"}), 400

        manager.delete_asset(asset)
        return jsonify({
            "status": "deleted",
            "asset": asset
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():