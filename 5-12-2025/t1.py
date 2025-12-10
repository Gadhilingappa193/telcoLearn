from typing import Annotated
from annotated_types import Gt, Len, Predicate
from pydantic import BaseModel
import json
import loggin

# with open(r'demo.json','r') as file:
#     demo = json.load(file)    
# print(demo)
demo={
    'A': 56,
    'B': "gfdhgfc"
}

class abc(BaseModel):
    A: int
    B: str
       
try:
    u=abc(**demo)
    print(u.A)
    print(u.B)
except:
    print("wrong value")