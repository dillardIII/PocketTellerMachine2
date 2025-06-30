from ghost_env import INFURA_KEY, VAULT_ADDRESS

from flask import Blueprint, render_template

real-time_trend_analysis_bp = Blueprint('real-time_trend_analysis_bp', __name__)

@real-time_trend_analysis_bp.route('/real-time_trend_analysis')
def show_real-time_trend_analysis():
    return render_template('real-time_trend_analysis.html')
