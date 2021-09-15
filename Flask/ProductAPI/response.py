
from flask import Flask

app = Flask(__name__) # inicializa flask

# rutas
@app.route("/")
def index():
    return "<h1>Bad Request</h1>",400

#inicia server
if __name__ == "__main__":
    app.run(debug=True, port=4000)




