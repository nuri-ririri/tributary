import requests

# url = 'http://0.0.0.0:8000/record'
# data = {'engine_temperature': 0.3}
# headers = {'Content-type': 'application/json'}

# response = requests.post(url, json=data, headers=headers)
response = requests.post("http://127.0.0.1:8000/record", json={"engine_temperature": 0.3})
# print('Status Code: ', response.status_code)
# print('Response: ', response.text)