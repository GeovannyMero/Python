from auth import auth as auth_blueprint
from flask import Flask;

app = Flask(__name__)
app.register_blueprint(auth_blueprint, url_prefix='/auth')

# def create_app(config_name):
#     app.register_blueprint(auth_blueprint, url_prefix='/auth')
#     return app

if __name__ == '__main__':
    app.run(port=4040, debug=True)