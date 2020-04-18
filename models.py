from app import db

class Reading(db.Model):
    __tablename__ = 'readings'
    id =  db.Column(db.Integer, primary_key=True)
    baro_temp = db.Column(db.Float)
    baro_pressure = db.Column(db.Float)
    cpu_temp = db.Column(db.Float)
    humid_temp = db.Column(db.Float)
    humid_humid = db.Column(db.Float)
    light = db.Column(db.Integer)
    time = db.Column(db.Float)
    soil_moisture = db.Column(db.Float)
    water_level = db.Column(db.Float)
    pump_status = db.Column(db.Float)

    def __init__(self, baro_temp, baro_pressure, cpu_temp, humid_temp, humid_humid, light, time, soil_moisture, water_level, pump_status):
        self.baro_temp = baro_temp
        self.baro_pressure = baro_pressure
        self.cpu_temp = cpu_temp
        self.humid_temp = humid_temp
        self.humid_humid = humid_humid
        self.light = light
        self.time = time
        self.soil_moisture = soil_moisture
        self.water_level = water_level
        self.pump_status = pump_status

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return({
            'id': self.id,
            'baro_temp': self.baro_temp,
            'baro_pressure': self.baro_pressure,
            'cpu_temp': self.cpu_temp,
            'humid_temp': self.humid_temp,
            'humid_humid': self.humid_humid,
            'light':self.light,
            'time': self.time,
            'soil_moisture': self.soil_moisture,
            'water_level': self.water_level,
            'pump_status': self.pump_status
        })
