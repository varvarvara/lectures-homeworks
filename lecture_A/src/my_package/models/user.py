from pydantic import BaseModel, Field, EmailStr, AnyHttpUrl, SecretStr
from pydantic import UUID4
from uuid import uuid4

class User(BaseModel):
    id: UUID4 = Field(default_factory=uuid4, description="user id")
    email: EmailStr = Field(description="user email")
    name: str = Field(description="user name")
    age: int = Field(description="user age")
    personal_website: AnyHttpUrl = Field(description="user personal website")
    password: SecretStr = Field(description="user password")
    
if __name__ == "__main__":
    user: User = User(
        email="user@example.com",
        name="John Doe",
        age=30,
        personal_website="https://example.com",
        password="secret123"
    )

    print(user)
