from pydantic import BaseModel, EmailStr, Field, field_validator

class UserRegistration(BaseModel):
    username: str = Field(min_length=5)
    email: EmailStr
    age: int = Field(ge=18)


# Example usage
user2 = UserRegistration(username="john Doe", email="john_doe@gmai.com", age=18)
print(user2)