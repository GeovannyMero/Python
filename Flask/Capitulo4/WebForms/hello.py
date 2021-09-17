from typing_extensions import Required
from flask_wtf import Form
# from flask import Flask
from wtforms import StringField, SubmitField
from wtforms.validators import required

class NameForm(Form):
    name = StringField("What is your name?", validators=[Required()])
    submit = SubmitField("Submit")

# app = Flask(__name__)
# app.config["SECRET_KEY"] = "hard to guess string"
