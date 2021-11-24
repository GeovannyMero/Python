import re
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from flask_login import UserMixin, login_required
from . import login_manager


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = \
    "sqlite:///"+os.path.join(basedir,"data.sqlite")
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index= True)
    password_hash = db.Column(db.String(128))
    # relaciones
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    @property
    def password(self):
        raise AttributeError('password is nor a readble attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(int(user_id))
    
    # @app.route('/secret')
    # @login_required
    # def secret():
    #     return 'Only authenticated users are allowed!'
    # def __repr__(self):
    #     return "<User %r>" % self.username

     
# db.create_all()
u = User()
u.password = 'cat'
u.password_hash
# print(u.password_hash)
u.verify_password('cat')