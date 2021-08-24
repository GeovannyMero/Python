from flask import Flask, json, jsonify
from products import products

app = Flask(__name__)

#rutas
@app.route("/ping")
def ping():
    return jsonify({"mensaje":"pong"})

@app.route("/products")
def getProducts():
    return jsonify({"products": products})

@app.route("/products/<string:name>")
def getProduct(name):
    print(name)
    productFound = [product for product in products if product["nombre"] == name]
    print(productFound)

    if(len(productFound) > 0):
        return jsonify({"product": productFound[0]})
    else:
        return jsonify({"mensaje": "No encontrado"})

# Inicia el servidor
if __name__ == '__main__':
    app.run(debug=True, port=4000)

