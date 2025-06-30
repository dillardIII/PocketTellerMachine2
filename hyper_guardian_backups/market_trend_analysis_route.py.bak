# market_trend_analysis_route.py – Handles real-time market trend evaluation

from flask import Blueprint, jsonify, request

market_trend_bp = Blueprint('market_trend', __name__)

@market_trend_bp.route("/api/market-trend", methods=["GET"])
def market_trend():
    route = request.args.get("route")

    if route == "market":
        return jsonify({
            "trend": "bullish",
            "confidence": 82,
            "timestamp": "2025-05-31T00:00:00Z"
        })
    else:
        return jsonify({"error": "Unknown route"}), 400