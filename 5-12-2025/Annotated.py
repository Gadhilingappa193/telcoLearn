from typing import Annotated
from annotated_types import Gt, Len, Predicate
from pydantic import BaseModel



# def is_prime(n):
#     if n <=1:
#         return False
#     for i in range (2, int(n**0.5)+1):
#         if n%i == 0:
#             return False
#         return True

class MyClass(BaseModel):
    age: Annotated[int, Gt(18)]
    # factors: list[Annotated[int, Predicate(is_prime)]]
    my_list: Annotated[list[int], Len(0, 10)] 
    
    
obj = MyClass(age = 35 , my_list = [1, 2, 3])
print(obj)
# obj.age = 25
# obj.my_list = [1, 2, 3, 4, 5]
# print(obj.age)
# print(obj.my_list)