from ghost_env import INFURA_KEY, VAULT_ADDRESS

from flask import Blueprint, render_template

assistant_voice_switcher_bp = Blueprint('assistant_voice_switcher_bp', __name__)

@assistant_voice_switcher_bp.route('/assistant_voice_switcher')
def show_assistant_voice_switcher():
    return render_template('assistant_voice_switcher.html')
