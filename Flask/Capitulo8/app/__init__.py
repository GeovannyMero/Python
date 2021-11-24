from flask_login.utils import login_fresh
from auth import auth as auth_blueprint
from flask import Flask;
from flask_login import LoginManager

app = Flask(__name__)
app.register_blueprint(auth_blueprint, url_prefix='/auth')
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app)

# def create_app(config_name):
#     app.register_blueprint(auth_blueprint, url_prefix='/auth')
#     login_manager.init_app(app)
#     return app


if __name__ == '__main__':
    app.run(port=4040, debug=True)