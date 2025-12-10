from typing import Annotated
from annotated_types import Gt, Len, Predicate
from pydantic import BaseModel
import requests
from datetime import datetime
import json

url = "https://api.nationalize.io/?name=gadhi"
data = None

for i in range(1,100): 
    response = requests.get(url)
    print(F"{i}--response")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"{i} -- {timestamp} -- {data}")

print("\nLast API Response:")
print(data)
    
# print("status code",response.status_code)

# for i=1; i<100; i++:
#     response = requests.get(url)
#     data = response.json()
#     print(F"{i}--response")
# print(data)
    