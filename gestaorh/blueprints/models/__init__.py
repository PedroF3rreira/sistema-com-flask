from flask import Blueprint

from .employee import Employee
from .user import User


bp = Blueprint("models", __name__)


def init_app(app):
    app.register_blueprint(bp)