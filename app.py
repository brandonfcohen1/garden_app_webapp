from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
from datetime import datetime

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Reading


@app.route("/", methods = ['GET'])
def dashboard(n_readings = 72):
    # Get last 6 hours of readings, dump to dataframe
    last360 = Reading.query.order_by(Reading.time.desc()).limit(n_readings).all()
    read_df = []
    for read in last360:
        json = read.serialize()
        json.update({'datetime': datetime.fromtimestamp(json['time'])})
        read_df.append(json)
    read_df = pd.DataFrame(read_df)
    read_df = read_df[read_df['time']>0]

    # Create figure, add subplots
    fig = plt.figure(figsize=(14,8.5))
    plt.subplots_adjust(hspace = 0.4)

    fig.add_subplot(331)
    plt.plot(read_df['datetime'], read_df['baro_temp'])
    plt.title('Temperature (from baro sensor)')
    plt.ylabel('deg F')

    fig.add_subplot(332)
    plt.plot(read_df['datetime'], read_df['humid_temp'])
    plt.title('Temperature (from humidity sensor)')
    plt.ylabel('deg F')

    fig.add_subplot(333)
    plt.plot(read_df['datetime'], read_df['cpu_temp'])
    plt.title('CPU Temperature')
    plt.ylabel('deg F')

    fig.add_subplot(334)
    plt.plot(read_df['datetime'], read_df['baro_pressure'])
    plt.title('Barometric Pressure')
    plt.ylabel('mmHg')

    fig.add_subplot(335)
    plt.plot(read_df['datetime'], read_df['humid_humid'])
    plt.title('Humidity')
    plt.ylabel('%')

    fig.add_subplot(336)
    plt.plot(read_df['datetime'], 1-read_df['light'])
    plt.title('Light')
    plt.ylabel('Light on?')

    fig.add_subplot(337)
    plt.plot(read_df['datetime'], read_df['soil_moisture'])
    plt.title('Soil Moisture')

    fig.add_subplot(338)
    plt.plot(read_df['datetime'], read_df['water_level'])
    plt.title('Water Level')

    fig.add_subplot(339)
    plt.plot(read_df['datetime'], read_df['pump_status'])
    plt.title('Pump Status')

    #Export to HTML
    return render_template('home.html', dashboard = str(mpld3.fig_to_html(fig)))


@app.route("/latest", methods = ['GET'])
def home_page():
    last_rec = Reading.query.order_by(Reading.id.desc()).first()
    last_rec = last_rec.serialize()
    df = pd.DataFrame(last_rec, index = [last_rec['id']]).drop(columns = 'id').to_html()

    return render_template('latest.html', last_result = df)


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
        time = content["time"],
        soil_moisture = content["soil_moisture"],
        water_level = content["water_level"],
        pump_status = content["pump_status"]
    )
    db.session.add(reading)
    db.session.commit()
    return "Record Added {}".format(reading.id)
