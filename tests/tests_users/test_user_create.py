import pytest
import allure
import requests
from conftest import user_data_new
from src.urls import Urls
from src.messages import *
from src.data import *

class TestUserCreate:

    @allure.title('Cоздание уникального юзера')
    def test_create_new_user(self, user_data_new):
        response = requests.post(Urls.url_user_create, json=user_data_new)
        response_data = response.json()
        assert response.status_code == 200
        delete_user(response_data["user"]["email"], response_data["accessToken"])


    @allure.title('Cоздание юзера, который уже зарегистрирован')
    def test_create_two_same_users(self, user_data_new):
        payload = {
            "email": user_data_new["email"],
            "password": user_data_new["password"],
            "name": user_data_new["name"]
        }
        response_1 = requests.post(Urls.url_user_create, json=payload)
        response_data = response_1.json()
        response_2 = requests.post(Urls.url_user_create, json=payload)
        assert response_2.status_code == 403
        assert response_2.json()["message"] == user_already_exists
        delete_user(response_data["user"]["email"], response_data["accessToken"])

    @allure.title("Создание без без обязательного поля") # ответ на запрос не соответствует документации
    def test_create_user_password_is_empty(self, user_data_new):
        user_data_new.pop("password")
        response = requests.post(Urls.url_user_create, json=user_data_new)
        assert response.status_code == 403
        assert response.json()["message"] == empty_required_field