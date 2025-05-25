
from flask import Blueprint, render_template

fallback_feature_bp = Blueprint('fallback_feature_bp', __name__)

@fallback_feature_bp.route('/fallback_feature')
def show_fallback_feature():
    return render_template('fallback_feature.html')
