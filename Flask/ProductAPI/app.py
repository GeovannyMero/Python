from flask import Flask,jsonify, request
from products import products

app = Flask(__name__)

#rutas
@app.route("/ping")
def ping():
    return jsonify({"mensaje":"pong"})

@app.route("/products")
def getProducts():
    return jsonify({"products": products})

@app.route("/products/<string:name>") # Usan parametros
def getProduct(name):
    print(name)
    productFound = [product for product in products if product["nombre"] == name]
    print(productFound)

    if(len(productFound) > 0):
        return jsonify({"product": productFound[0]})
    else:
        return jsonify({"mensaje": "No encontrado"})


@app.route("/product", methods=["POST"])
def addProduct():
    nuevoProducto = {
        "nombre": request.json["nombre"],
        "precio": request.json["precio"],
        "cantidad": request.json["cantidad"]
    }
    products.append(nuevoProducto)
    print(request.json)
    return jsonify({"products": products})

# actualizar
@app.route("/product/<string:nombre>", methods=["PUT"])
def updateProduct(nombre):
    return 'update'

# delete
@app.route("/product/<string:name>", methods=["DELETE"])
def deleteProduct(name):
    return "delete"

# Inicia el servidor
if __name__ == '__main__':
    app.run(debug=True, port=4000)

