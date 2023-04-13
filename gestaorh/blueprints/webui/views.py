from flask import abort, render_template
from gestaorh.blueprints.models.user import User
from gestaorh.ext.database import db
from flask_simplelogin import login_required
from flask.views import MethodView


def admin():
	return render_template('index.html', title='home page')

page_login_required = login_required(admin)