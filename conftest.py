import pytest
from src.data import *



@pytest.fixture
def user_data_new_with_delete():
    payload = generate_user_data()

    response = requests.post(Urls.url_user_create, json=payload)
    yield response
    response_data = response.json()
    delete_user(response_data["user"]["email"], response_data["accessToken"])
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
