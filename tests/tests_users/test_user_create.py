
import allure
import requests
from conftest import user_data_with_delete_user, user_data_new
from src.urls import Urls
from src.messages import *
from src.generator.user_data_generator import *
from src.api.user_api import *

class TestUserCreate:

    @allure.title('Cоздание уникального юзера')
    def test_create_new_user(self):
        payload = {
            "email": generate_user_data()["email"],
            "password": generate_user_data()["password"],
            "name": generate_user_data()["name"]
        }
        response = requests.post(Urls.url_user_create, json=payload)

        assert response.status_code == 200
        response_data = response.json()
        delete_user(response_data["user"]["email"], response_data["accessToken"])



    @allure.title('Cоздание юзера, который уже зарегистрирован')
    def test_create_two_same_users(self, user_data_with_delete_user):
        payload = {
            "email": user_data_with_delete_user["email"],
            "password": user_data_with_delete_user["password"],
            "name": user_data_with_delete_user["name"]
        }
        response = requests.post(Urls.url_user_create, json=payload)

        assert response.status_code == 403
        assert response.json()["message"] == user_already_exists

    @allure.title("Создание без обязательного поля пароль")
    def test_create_user_password_is_empty(self, user_data_new):
        user_data_new.pop("password")
        response = requests.post(Urls.url_user_create, json=user_data_new)
        assert response.status_code == 403
        assert response.json()["message"] == empty_required_field