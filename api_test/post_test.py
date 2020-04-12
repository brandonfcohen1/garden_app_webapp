import requests

url = 'http://127.0.0.1:5000/api/add'

reading = {
   "baro_pressure": 0.0,
   "baro_temp": 0.0,
   "cpu_temp": 0.0,
   "humid_humid": 0.0,
   "humid_temp": 0.0,
   "light": 0,
   "reading_id": 0,
   "time": 0.0
 }

print(requests.post(url, json = reading).text)
