import allure
import requests
from conftest import user_data_with_delete_user
from src.urls import Urls
from src.messages import *
from src.data import *


class TestUserlogin:

    def test_user_login_after_registration(self, user_data_with_delete_user):
        payload = {
            "email": user_data_with_delete_user["email"],
            "password": user_data_with_delete_user["password"],
            "name": user_data_with_delete_user["name"]
        }
        response = requests.post(Urls.url_user_login, json=payload)
        assert response.status_code == 200
        assert response.json()["success"] == True


    def test_user_login_with_invalid_email(self, user_data_with_delete_user):
        payload = {
            "email": f'{user_data_with_delete_user["email"]}com',
            "password": user_data_with_delete_user["password"],
            "name": user_data_with_delete_user["name"]
        }
        response = requests.post(Urls.url_user_login, json=payload)

        assert response.status_code == 401
        assert response.json()["message"] == incorrect_fields


    def test_user_login_with_invalid_password(self, user_data_with_delete_user):
        payload = {
            "email": user_data_with_delete_user["email"],
            "password": f'{user_data_with_delete_user["password"]}123',
            "name": user_data_with_delete_user["name"]
        }
        response = requests.post(Urls.url_user_login, json=payload)

        assert response.status_code == 401
        assert response.json()["message"] == incorrect_fields

