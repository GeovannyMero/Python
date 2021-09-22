import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.orm import backref

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = \
    "sqlite:///"+os.path.join(basedir,"data.sqlite")
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    # relaciones
    users = db.relationship("User", backref="role")

    def __repr__(self):
        return "<Role %r>" % self.name

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index= True)

    # relaciones
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self):
        return "<User %r>" % self.username


# db.create_all()
# admin_role = Role(name="Admin")
# mod_role = Role(name="Moderador")
# user_role = Role(name="User")
# user_john = User(username="john", role=admin_role)
# user_susan = User(username="susan", role=user_role)

# db.session.add_all([admin_role,mod_role,user_role,user_john, user_susan])

# db.session.commit()

# print(admin_role.id)
print(Role.query.all())
print(User.query.all())