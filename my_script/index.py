import requests
import json

# url_api = "http://api.aladhan.com/v1/timingsByCity?city=Cairo&country=Egypt&method=5"

# response = requests.get(url=url_api)

# print(response.json())

url_api = "http://host.docker.internal:5000/incomes"

method = input('GET OR POST : ')

if method=='GET' :
    response = requests.get(url_api)
    print(response.json())

elif method=='POST' :
    amount = int(input('Enter amount: '))
    d = { 'description': 'salary', 'amount': amount }
    response = requests.post(url=url_api, json=json.dumps(d))
    print(response.status_code)

else :
    print('Not allowed')


