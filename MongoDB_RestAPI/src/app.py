from flask import Flask, jsonify, Response
from flask_pymongo import MongoClient
from bson import json_util

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb+srv://m001-student-gm:Admin123@sandboxgm.uufnr.mongodb.net/SandboxGM?retryWrites=true&w=majority"
mongo = MongoClient("mongodb+srv://m001-student-gm:Admin123@sandboxgm.uufnr.mongodb.net/SandboxGM?retryWrites=true&w=majority")

# Database
Database = mongo.get_database("sample_training")

# Table
SampleTable = Database.zips

@app.route("/", methods=['GET'])
def get():
    p =  SampleTable.find({"state":"NY"})
    response = json_util.dumps(p)
    return Response(response,mimetype='application/json')
    # return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)