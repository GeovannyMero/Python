import os
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.orm import backref
from flask_wtf import Form
from flask import Flask, render_template, session
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
bootstrap = Bootstrap(app)
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
# print(Role.query.all())
# print(User.query.all())

app.config["SECRET_KEY"] = "hard to guess string"

class NameForm(Form):
    name = StringField("What is your name?")
    submit = SubmitField("Submit")

@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session["known"] = False
        else:
            session["known"] = True
        session["name"] = form.name.data
        form.name.data = ""
        return redirect(url_for("index"))
    return render_template("index.html", form=form, name = session.get('name'), known = session.get("known", False))

if __name__ == "__main__":
    app.run(debug=True, port=4000)