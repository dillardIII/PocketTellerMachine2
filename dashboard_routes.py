from flask import Blueprint, render_template

dashboard_routes = Blueprint('dashboard_routes', __name__)

# === Main Dashboard View ===
@dashboard_routes.route('/dashboard')
def dashboard_view():
    return render_template('dashboard.html')

# === Example Diagnostic Route (Original) ===
@dashboard_routes.route('/diagnostics')
def run_diagnostics():
    return "Diagnostics running..."

# === Example Diagnostic Route (Added as Requested) ===
@dashboard_routes.route('/diagnostics_alt')
def run_diagnostics_alt():
    return "Diagnostics page is working!"