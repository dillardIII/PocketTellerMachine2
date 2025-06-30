from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
from flask import Blueprint, jsonify, render_template, request
from congress_tracker import get_congress_influence

# === Create Flask Blueprint(===)
congress_overlay_bp = Blueprint('congress_overlay', __name__)

# === Route: Congress Influence API ===
@congress_overlay_bp.route('/api/congress_influence', methods=['GET'])
def api_congress_influence():
    symbol = request.args.get('symbol', 'AAPL')
    influence_score = get_congress_influence(symbol)
    
    return jsonify({
        'symbol': symbol.upper(),
        'influence_score': influence_score
    })

# === Route: Congress Overlay Dashboard ===
@congress_overlay_bp.route('/congress_overlay')
def congress_overlay_page():
    default_symbol = 'AAPL'
    influence_score = get_congress_influence(default_symbol)
    
    return render_template('congress_overlay.html', symbol=default_symbol, influence_score=influence_score)

def log_event():ef drop_files_to_bridge():