from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField
from flask_wtf import Form

class NameForm(Form):
    name = StringField("What is your name?")
    submit = SubmitField("Submit")