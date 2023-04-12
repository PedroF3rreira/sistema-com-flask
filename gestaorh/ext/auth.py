from flask_simplelogin import SimpleLogin
from gestaorh.blueprints.models import User
from flask import request
from werkzeug.security import check_password_hash, generate_password_hash

def login_check(credentials):

	user = User.query.filter_by(name=credentials.get('username')).first()
	secret = generate_password_hash(credentials.get('password'))
	
	if user and check_password_hash(secret, credentials.get('password')):
		return True
	return False


def init_app(app):
	SimpleLogin(app, login_checker=login_check)
