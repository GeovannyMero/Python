from flask import Flask, jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/test'

mongo = PyMongo(app)


@app.route('/ping')
def ping():
    return jsonify({'message': 'pong'})

@app.route('/contribuyentes')
def get_all():
    contri = mongo.db.contribuyente.find({'estado_contribuyente':'ACTIVO'})
    response = json_util.dumps(contri)
    return Response(response, mimetype='application/json')


@app.route('/contribuyentes/<ruc>')
def get_by_ruc(ruc):
    contri = mongo.db.contribuyente.find_one({'ruc':ruc})
    response = json_util.dumps(contri)
    return Response(response, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=4000)