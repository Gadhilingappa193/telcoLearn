import requests, json

url = "http://api.ipapi.com/api/161.185.160.93?access_key=44a37b471413795e084ae5b6ab3e5ea2"

response = requests.get(url)

print("source code",response.status_code)

try:
    response.status_code == 200
    
    print(response.json())
    
except:
   
    print("error")