from flask_bootstrap import Bootstrap
from flask import Flask, render_template
# bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("users.html", name=name)

# MANEJO DE ERRORES DE HTTP
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True, port=4000)