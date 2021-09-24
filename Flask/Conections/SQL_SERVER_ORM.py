from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import urllib

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = 'Driver={SQL Server};Server=DESKTOP-RROBOR5;Database=MediSoft;Trusted_Connection=yes;'
params = urllib.parse.quote_plus('Driver={SQL Server};Server=DESKTOP-RROBOR5;Database=MediSoft;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class City(db.Model):
    __tablename__ = "City"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))

    def __repr__(self):
        return "<City %r>" % self.description

print(City.query.all())