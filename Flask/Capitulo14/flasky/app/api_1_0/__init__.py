from flask import Blueprint, Flask

api = Blueprint('api', __name__)

from . import user, commets

app = Flask(__name__)

def create_app(config_name):
    from api_1_0 import api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')    