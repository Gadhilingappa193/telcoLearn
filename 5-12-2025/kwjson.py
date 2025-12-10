from typing import Annotated
from annotated_types import Gt, Len, Predicate
from pydantic import BaseModel
import json
import loggin

# with open(r'demo.json','r') as file:
#     demo = json.load(file)    
# print(demo)
demo={
    "uid": 1,
    "name": "gadhilingappa",
    "signup": "2025-01-05T10:30:00",
    "tastes": {
        "sweet": 3,
        "hot": 5
    }
}

class user(BaseModel):
    uid: int
    name: str = "gadhi"
    signup: datetime | None
    tastes: dict[str, int]
       
try:
    u=user(**demo)
    print(u.A)
    print(u.B)
except:
    print("wrong value")