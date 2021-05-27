import json
import re
import requests



data=requests.get('http://127.0.0.1:8000/clean/')
data=data.json()

for i in data:
    data=i['nameofvideo']
    excluding=re.search('17',data)
    if excluding:
        print(data)
    else:
        print('no')
