from flask import Flask
from src.routes.contribuyente import contri

app = Flask(__name__)

# @app.route('/contribuyentes')
# def get_all():
#     contri = mongo.db.contribuyente.find({'estado_contribuyente':'ACTIVO'})
#     response = json_util.dumps(contri)
#     return Response(response, mimetype='application/json')

app.register_blueprint(contri)

if __name__ == '__main__':
    app.run(debug=True, port=4000)