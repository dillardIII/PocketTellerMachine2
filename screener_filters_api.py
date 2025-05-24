import os
import json
from flask import Blueprint, request, jsonify

FILTERS_FILE = "data/screener_filters.json"

market_screener_filters_bp = Blueprint('market_screener_filters', __name__)

@market_screener_filters_bp.route('/api/screener_filters', methods=['GET'])
def get_screener_filters():
    if os.path.exists(FILTERS_FILE):
        with open(FILTERS_FILE, "r") as f:
            filters = json.load(f)
        return jsonify(filters)
    else:
        return jsonify({
            "rsi": {"min": None, "max": None},
            "volume": {"min": None},
            "price": {"min": None, "max": None}
        })

@market_screener_filters_bp.route('/api/screener_filters', methods=['POST'])
def update_screener_filters():
    try:
        filters = request.get_json()

        with open(FILTERS_FILE, "w") as f:
            json.dump(filters, f, indent=2)

        return jsonify({"status": "success", "message": "Filters updated."})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500