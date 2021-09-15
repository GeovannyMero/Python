from flask import Flask
from flask.helpers import make_response


app = Flask(__name__)

@app.route("/")
def index():
    response = make_response("<h1>Este documento contiene cookies</h1>")
    response.set_cookie("res", "42")
    return response

if __name__ == "__main__":
    app.run(debug=True, port=4000)