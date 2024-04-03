from flask import Blueprint, jsonify, Response
import tomllib
from flask_pymongo import MongoClient
from bson import json_util
import json
import pprint

contri = Blueprint('contribuyente', __name__, url_prefix='/contri')

# Obtener configuración
conf = None

with open('Config.toml', 'rb') as f:
    conf = tomllib.load(f)

db_url = conf['MONGODB']['uri'] # 'mongodb://localhost/'
client = MongoClient(db_url)
db = client.test.contribuyente

# @app.errorhandler(404)
# def not_found(error=None):
#     response = jsonify({
#         'message': 'Resoruce Not Found',
#         'status': 404
#     })
#     response.status_code = 404
#     return response


@contri.route('/')
def get_all():
    return jsonify({'message': 'pong'})


@contri.route('/ruc/<ruc>')
def get_by_ruc(ruc):
    data = db.find_one({'ruc':ruc})
    response = None

    if data is None or data == '':
        result = {
            'message': 'No existe información',
            'data': {}
        }
        response = Response(json_util.dumps(result), status=404, mimetype='application/json')
    else:
        result = {
            'message': 'OK',
            'data': data
        }
        response = Response(json_util.dumps(result), status=200,mimetype='application/json')
    
    return response

@contri.route('/provincia/<provincia>')
def get_by_province(provincia):

    if provincia != '':
        # return f'La provincia es: {provincia}' {'provincia_juridiccion': provincia.upper()}
        data = db.find().limit(2)
        # list_data = list(data)
        count = len(list(data))
        arr = list(db.find({'provincia_juridiccion': provincia.upper()}).limit(10))
        # print(json_util.dumps(arr))
        # print(len(arr))

        #for item in list(db.find().limit(2)):
            # pprint.pprint(item)
        #    print(item)

      
        if len(arr) == 0:
            result = {
                'message': 'No existe información para la provincia ingresada',
                'data': {}
            }
            response = Response(json_util.dumps(result), status=404, mimetype='application/json')
        else:
            result = {
               'message': 'OK',
               'data': arr
            }
            response = Response(json_util.dumps(arr), status=200, mimetype='application/json')
        return response
    else:
        return 'no'  

