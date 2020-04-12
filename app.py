from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Reading


@app.route("/getall", methods = ['GET'])
def get_all():
    readings=Reading.query.all()
    return jsonify([r.serialize() for r in readings])

@app.route("/last/<int:limrecs>", methods = ['GET'])
def get_last_record(limrecs):
    last_n=Reading.query.order_by(Reading.id.desc()).limit(limrecs)
    return jsonify([r.serialize() for r in last_n])


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
