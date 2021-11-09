
import re
from flask.app import Flask
from flask_httpauth import HTTPBasicAuth, g
from werkzeug.exceptions import Unauthorized
from Flask.Capitulo14.flasky.app.api_1_0.errors import forbidden

from Flask.Capitulo7.flasky.app.models import User

auth = HTTPBasicAuth
api = Flask(__name__)

@auth.verify_password
def verify_password(email, password):
    if email == '':
        auth.current_user  = 'invitado'
        return True
    user = User.query.filter_by(email = email).first()
    if not user:
        return False
    auth.current_user=user
    return user.verify_password(password)


@auth.error_handler
def auth_error():
    return Unauthorized('Invalid credentiasl')

@api.route('/posts')
@auth.login_required
def get_posts():
    pass


@api.before_request
@auth.login_required
def before_request():
    if not auth.current_user.is_anonymous and \
        not auth.current_user.confirmed:
        return forbidden("Unconfirmed account")
