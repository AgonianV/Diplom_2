import pytest
from src.api.user_api import *
from src.generator.user_data_generator import generate_user_data


@pytest.fixture
def user_data_new():
    payload = generate_user_data()
    yield payload

@pytest.fixture
def user_data_with_delete_user():
    email, password, name, token = register_new_user_and_return_login_password()
    payload = {
        "email": f"{email}@yandex.ru",
        "password": password,
        "name": name,
        "token": token
    }

    yield payload

    delete_user(email, token)
