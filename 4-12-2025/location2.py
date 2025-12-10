import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=13.1377&longitude=78.13&daily=weather_code,sunrise,daylight_duration,sunshine_duration,rain_sum,showers_sum,snowfall_sum,precipitation_sum,precipitation_hours,precipitation_probability_max&hourly=temperature_2m,weather_code&current=temperature_2m,rain,weather_code,cloud_cover,showers,is_day"
response = requests.get(url)
datas = response.json()
print("status code",response.status_code)
print("response",datas)


json = json.dumps(datas, indent=4)
with open(r"C:\Users\ADMIN\OneDrive\Desktop\telcom\4-12-2025\location2.json", "w") as f:
    f.write(json)