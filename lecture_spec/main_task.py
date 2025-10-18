
class User:
    pwd: str
    name: str

user = User(
    name = "Вася",
    pwd = "12345"
)

def foo(user: User):
    print(user.name)
    

import pydantic
from pydantic import BaseModel

class User(BaseModel):
    name: str
    pwd: str

user = User(
    name = 5,
    pwd = "fdef"
)

d = {'name': 'kdovk', 'pwd': 'fdef'}
print(User.model_validate(d))