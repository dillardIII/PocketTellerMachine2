from ghost_env import INFURA_KEY, VAULT_ADDRESS

from flask import Blueprint, render_template

risk_assessment_dashboard_bp = Blueprint('risk_assessment_dashboard_bp', __name__)

@risk_assessment_dashboard_bp.route('/risk_assessment_dashboard')
def show_risk_assessment_dashboard():
    return render_template('risk_assessment_dashboard.html')
