import requests

prod = 'http://cohengarden.herokuapp.com/getall'
local = 'http://127.0.0.1:5000/api/add'

if "prod_data" not in globals():
    prod_data = requests.get(prod).json()

for rec in prod_data:
    requests.post(local, json = rec)
    print(rec['id'])