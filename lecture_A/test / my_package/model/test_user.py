import pytest

from pydantic import AnyHttpUrl, SecretStr
from my_package.models.user import User



def test_user_creation():

    email = "john.doe@example.com"
    name = "John Doe"
    age = 30
    personal_website = "https://john.doe.com"
    password = "password123"
    user = User(

        email=email,
        name=name,
        age=age,
        personal_website=AnyHttpUrl(personal_website),
        password=SecretStr(password),

    )

    assert user.email == email
    assert user.name == name
    assert user.age == age
    assert user.personal_website == AnyHttpUrl(personal_website)
    assert user.password == SecretStr(password)
    assert user.password.get_secret_value() == password


