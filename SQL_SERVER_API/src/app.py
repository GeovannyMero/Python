from dataclasses import dataclass
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import urllib

app = Flask(__name__)

params = urllib.parse.quote_plus('Driver={SQL Server};Server=DESKTOP-RROBOR5;Database=MediSoft;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

@dataclass
class City(db.Model):
    # schema json
    id: int
    description: str

    # Campos de la tabla
    __tablename__ = "City"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))

    def __repr__(self):
        return "<City %r>" % self.description



@app.route("/city", methods=["GET"])
def city():
    # cities = City.query.all()
    cities = City.query.filter_by(description="Guayaquil").first()
    return jsonify(cities)



if __name__ == "__main__":
    app.run(debug=True, port=5000)







