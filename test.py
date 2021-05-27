import json
import re
import requests
import datetime



data=requests.get('http://127.0.0.1:8000/clean/')
data=data.json()

for i in data:
    data=i['nameofvideo']
    NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
    formatted= NextDay_Date.strftime("%y-%m-%d")
    excluding=re.search(formatted,data)
    if excluding:
        print(data)




# from datetime import datetime

# now = datetime.now()

# current_time = now.strftime("%H-%M-%S")
# print("Current Time =", current_time)


# print (formatted)