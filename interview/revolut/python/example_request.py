import json

import requests
from requests.auth import HTTPBasicAuth

url = 'http://127.0.0.1:5000/nest'

with open('tests/data/input.json') as f:
    data = json.load(f)

params = {'levels': 'currency country city'}
res = requests.post(url, params=params, json=data, auth=HTTPBasicAuth('john', 'hello'))
print(res.json())
