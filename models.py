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

    def __init__(self, baro_temp, baro_pressure, cpu_temp, humid_temp, humid_humid, light, time):
        self.baro_temp = baro_temp
        self.baro_pressure = baro_pressure
        self.cpu_temp = cpu_temp
        self.humid_temp = humid_temp
        self.humid_humid = humid_humid
        self.light = light
        self.time = time

    def __repr__(self):
        return '<id {}>'.format(self.id)
