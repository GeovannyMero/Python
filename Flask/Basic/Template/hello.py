from flask_bootstrap import Bootstrap
# from flask import Flask, render_template
# from flask.templating import render_template
from flask_wtf import Form
from flask import Flask, render_template, session, redirect, url_for, flash
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Required
# bootstrap


app = Flask(__name__)
app.config["SECRET_KEY"] = "Pruebas geo"
bootstrap = Bootstrap(app)

class NameForm(Form):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/index", methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        # session["name"] = form.name.data
        old_name = session["name"]
        if old_name is not None and old_name != form.name.data:
            flash("Looks like you have changed your name!")
        session["name"] = form.name.data
        form.name.data = ""
        return redirect(url_for("index"))
        # name = form.name.data
        # form.name.data = ""
    return render_template("index2.html", form=form, name=session.get("name"))

@app.route("/user/<name>")
def user(name):
    return render_template("users.html", name=name)

# MANEJO DE ERRORES DE HTTP
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True, port=4000)