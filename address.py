from pydantic import BaseModel, EmailStr


class StreetAddress(BaseModel):
    street: str
    city: str
    zip_code: str


class UserandAddress(BaseModel):
    id: int
    name: str
    email: EmailStr  # Built-in validator for email format
    addresses: list[StreetAddress]  # List of nested Address models


# Valid data with nested structure
user_data = {
    "id": 2,
    "name": "Bob",
    "email": "nida@example.com",
    "addresses": [
        {"street": "123 saima", "city": "islamabad", "zip_code": "20091"},
        {"street": "afnan arcade", "city": "karachi", "zip_code": "456001"},
    ],
}
user = UserandAddress.model_validate(user_data)
print(user)

# Invalid data with nested structure
user_data = {
    "id": 2,
    "name": "Bob",
    "email": "nidz@example",
    "addresses": [
         {"street": "123 saima", "city": "islamabad", "zip_code": "20091"},
        {"street": "afnan arcade", "city": "karachi", "zip_code": "456001"},
    ],
}
try:
    user = UserandAddress.model_validate(user_data)
    print(user)
except Exception as e:
    print(e)
