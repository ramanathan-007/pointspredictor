import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Height':6.8, 'goals%':0.5, 'freethrows%':0.6})

print(r.json())