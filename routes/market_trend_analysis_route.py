from ghost_env import INFURA_KEY, VAULT_ADDRESS

from flask import Blueprint, render_template

market_trend_analysis_bp = Blueprint('market_trend_analysis_bp', __name__)

@market_trend_analysis_bp.route('/market_trend_analysis')
def show_market_trend_analysis():
    return render_template('market_trend_analysis.html')
