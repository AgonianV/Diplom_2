import requests
import allure
from src.urls import Urls
from src.helpers import generate_random_string

@allure.step('Удаление юзера')
def delete_user(email, token):
    payload = {"email": email}
    headers = {"Authorization": token}
    requests.delete(Urls.url_user_delete, headers=headers, json=payload)


@allure.step('метод регистрации нового пользователя')
def register_new_user_and_return_login_password():
    login_pass = []

    email = generate_random_string(10)
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": f"{email}@yandex.ru",
        "password": password,
        "name": name
    }

    response = requests.post(Urls.url_user_create, data=payload)
    response_data = response.json()

    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(name)
        login_pass.append(response_data["accessToken"])

    return login_pass