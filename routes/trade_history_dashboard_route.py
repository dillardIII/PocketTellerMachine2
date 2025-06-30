from ghost_env import INFURA_KEY, VAULT_ADDRESS

from flask import Blueprint, render_template

trade_history_dashboard_bp = Blueprint('trade_history_dashboard_bp', __name__)

@trade_history_dashboard_bp.route('/trade_history_dashboard')
def show_trade_history_dashboard():
    return render_template('trade_history_dashboard.html')
