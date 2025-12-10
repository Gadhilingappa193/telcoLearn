import requests, json
from typing import Annotated
from annotated_types import Gt, Len, Predicate
from pydantic import BaseModel

url1 = "https://api.open-meteo.com/v1/forecast?latitude=13.1377&longitude=78.13&daily=weather_code,sunrise,daylight_duration,sunshine_duration,rain_sum,showers_sum,snowfall_sum,precipitation_sum,precipitation_hours,precipitation_probability_max&hourly=temperature_2m,weather_code&current=temperature_2m,rain,weather_code,cloud_cover,showers,is_day"
url2 = "https://api.open-meteo.com/v1/forecast?latitude=15.4608&longitude=76.2883&daily=weather_code,sunrise,daylight_duration,sunshine_duration,rain_sum,showers_sum,snowfall_sum,precipitation_sum,precipitation_hours,precipitation_probability_max&hourly=temperature_2m&current=temperature_2m,rain,weather_code,cloud_cover,showers,is_day"

response1 = requests.get(url1)
response2 = requests.get(url2)
combined = [response1.json(), response2.json()]
print("status code",response1.status_code)
print("status code",response2.status_code)

with open(r"C:\Users\ADMIN\OneDrive\Desktop\telcom\4-12-2025\location_combined.json", "w") as f:
    json.dump(combined, f, indent=4)



with open(r'C:\Users\ADMIN\OneDrive\Desktop\telcom\4-12-2025\location_combined.json', 'r') as file:
    data = json.load(file)
print(data)