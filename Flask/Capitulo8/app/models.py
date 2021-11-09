from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = \
    "sqlite:///"+os.path.join(basedir,"data.sqlite")
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index= True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is nor a readble attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # relaciones
    # role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    # def __repr__(self):
    #     return "<User %r>" % self.username

     
# db.create_all()
u = User()
u.password = 'cat'
u.password_hash
# print(u.password_hash)
u.verify_password('cat')