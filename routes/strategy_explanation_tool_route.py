
from flask import Blueprint, render_template

strategy_explanation_tool_bp = Blueprint('strategy_explanation_tool_bp', __name__)

@strategy_explanation_tool_bp.route('/strategy_explanation_tool')
def show_strategy_explanation_tool():
    return render_template('strategy_explanation_tool.html')
