from ghost_env import INFURA_KEY, VAULT_ADDRESS
from flask import Blueprint, render_template, jsonify, request
from congress_tracker import get_congress_influence

# === Create Blueprint(for Congress Section in Dashboard ===)
dashboard_congress_bp = Blueprint('dashboard_congress', __name__)

# === Route: Dashboard Congress Section API ===
@dashboard_congress_bp.route('/api/dashboard/congress_influence', methods=['GET'])
def dashboard_congress_influence():
    symbol = request.args.get('symbol', 'AAPL')
    influence_score = get_congress_influence(symbol)
    
    return jsonify({
        'symbol': symbol.upper(),
        'influence_score': influence_score
    })

# === This will be used as a section in the main dashboard ===
@dashboard_congress_bp.route('/dashboard_congress_section')
def dashboard_congress_section():
    symbol = request.args.get('symbol', 'AAPL')
    influence_score = get_congress_influence(symbol)
    
    return render_template('dashboard_congress_section.html', symbol=symbol, influence_score=influence_score)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():