import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=15.4608&longitude=76.2883&daily=weather_code,sunrise,daylight_duration,sunshine_duration,rain_sum,showers_sum,snowfall_sum,precipitation_sum,precipitation_hours,precipitation_probability_max&hourly=temperature_2m&current=temperature_2m,rain,weather_code,cloud_cover,showers,is_day"
response = requests.get(url)
datas = response.json()
print("status code",response.status_code)
print("response",datas)


with open(r"C:\Users\ADMIN\OneDrive\Desktop\telcom\4-12-2025\location1.json", "w") as f:
    json = json.dumps(datas, indent=4)
    f.write(json)