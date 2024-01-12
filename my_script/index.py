import requests
import json

# url_api = "http://api.aladhan.com/v1/timingsByCity?city=Cairo&country=Egypt&method=5"

# response = requests.get(url=url_api)

# print(response.json())

url_api = "http://web_api:2500/incomes"

print('GET OR POST : ', flush=True)
method = input()

if method=='GET' :
    response = requests.get(url_api)
    print(response.json())

elif method=='POST' :
    print('Enter amount: ', flush=True)
    amount = int(input())
    d = { 'description': 'salary', 'amount': amount }
    response = requests.post(url=url_api, json=json.dumps(d))
    print(response.status_code)

else :
    print('Not allowed', flush=True)


