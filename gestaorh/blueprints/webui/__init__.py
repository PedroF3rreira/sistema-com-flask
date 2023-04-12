from flask import Blueprint
from .views import page_login_required
from .employee_views import index

bp = Blueprint("webui", __name__, template_folder="templates")

# USER
bp.add_url_rule("/", view_func=page_login_required, endpoint='home')


def init_app(app):
    app.register_blueprint(bp)