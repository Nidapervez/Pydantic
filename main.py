from pydantic import BaseModel,validators,EmailStr
class person(BaseModel):
    name: str
    age: int
    address: str
    email:EmailStr


try:
    P1=person(name="A",age=12,address="abc",email="nnpervez333@gmail.com")
    print(P1)
except Exception as e:
    print(e)

#error will raise if i will give wrong email type

try:
    P1=person(name="A",age=12,address="abc",email="nnpe.com")
    print(P1)
except Exception as e:
    print(e)
