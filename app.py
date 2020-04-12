from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Reading

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api/add", methods = ['POST'])
def add_record():
    content = request.json
    reading=Reading(
        baro_temp = content["baro_temp"],
        baro_pressure = content["baro_pressure"],
        cpu_temp = content["cpu_temp"],
        humid_temp = content["humid_temp"],
        humid_humid = content["humid_humid"],
        light = content["light"],
        time = content["light"]
    )
    db.session.add(reading)
    db.session.commit()
    return "Record Added {}".format(reading.id)
