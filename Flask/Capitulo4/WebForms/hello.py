from flask_wtf import Form
from flask import Flask, render_template, session
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"

class NameForm(Form):
    name = StringField("What is your name?")
    submit = SubmitField("Submit")


@app.route("/")
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
    return render_template("index.html", form=form, name=name)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

