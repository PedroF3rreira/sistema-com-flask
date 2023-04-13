from flask_simplelogin import SimpleLogin, Message
from gestaorh.blueprints.models import User
from flask import request
from werkzeug.security import check_password_hash, generate_password_hash


def login_check(credentials):
	user = User.query.filter_by(name=credentials.get('username')).first()

	if user and check_password_hash(user.password, credentials.get('password')):
		return True
	return False

messages = {
    'login_success': Message('Você está logado!'),  # the default CSS class is `primary`
    'login_failure': 'Não foi possivel fazer o login!',  # this also uses the default CSS class
    'is_logged_in': Message('Iam initium', 'success'), # this uses `success` as the CSS class
    'logout': None, # this disables the message for logout
    'login_required': Message('Você tem que fazer login para acessar o sistema'),
    'access_denied': 'Usuário não autorizado',
    'auth_error': 'Um erro ocorreu： {0}'
}


def init_app(app):
	SimpleLogin(app, login_checker=login_check, messages=messages)
