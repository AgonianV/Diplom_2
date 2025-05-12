import allure
import requests
from conftest import user_data_with_delete_user
from src.urls import Urls
from src.messages import *
from src.data import *

class TestUserDataChange:
    @allure.title("Изменение почты авторизованному пользователю")
    def test_user_change_email_with_auth(self, user_data_with_delete_user):
        payload = {
            "email": f'{user_data_with_delete_user["email"]}test'
        }
        headers = {"Authorization": user_data_with_delete_user["token"]}
        response = requests.patch(Urls.url_user_change_data, headers=headers, json=payload)
        assert response.status_code == 200
        assert response.json()["user"]["email"] == payload["email"]

    @allure.title("Изменение пароля авторизованному пользователю")
    def test_user_change_password_with_auth(self, user_data_with_delete_user):
        payload = {
            "email": user_data_with_delete_user["email"],
            "password": f'{user_data_with_delete_user["password"]}test',
            "name": user_data_with_delete_user["name"]
        }
        headers = {"Authorization": user_data_with_delete_user["token"]}
        response = requests.patch(Urls.url_user_change_data, headers=headers, json=payload)
        assert response.status_code == 200
        assert requests.post(Urls.url_user_login, json=payload).status_code == 200

    @allure.title("Изменение имени авторизованному пользователю")
    def test_user_change_name_with_auth(self, user_data_with_delete_user):
        payload = {
            "email": user_data_with_delete_user["email"],
            "password": user_data_with_delete_user["password"],
            "name": f'{user_data_with_delete_user["name"]}test'
        }
        headers = {"Authorization": user_data_with_delete_user["token"]}
        response = requests.patch(Urls.url_user_change_data, headers=headers, json=payload)
        assert response.status_code == 200
        assert requests.post(Urls.url_user_login, json=payload).status_code == 200

    @allure.title("Изменение почты неавторизованному пользователю")
    def test_user_change_email_without_auth(self, user_data_with_delete_user):
        payload = {
            "email": f'{user_data_with_delete_user["email"]}test',
        }

        response = requests.patch(Urls.url_user_change_data, json=payload)
        assert response.status_code == 401
        assert response.json()["message"] == no_auth

    @allure.title("Изменение пароля неавторизованному пользователю")
    def test_user_change_password_without_auth(self, user_data_with_delete_user):
        payload = {
            "email": user_data_with_delete_user["email"],
            "password": f'{user_data_with_delete_user["password"]}test',
            "name": user_data_with_delete_user["name"]
        }
        response = requests.patch(Urls.url_user_change_data, json=payload)
        assert response.status_code == 401
        assert response.json()["message"] == no_auth

    @allure.title("Изменение имени неавторизованному пользователю")
    def test_user_change_name_without_auth(self, user_data_with_delete_user):
        payload = {
            "email": user_data_with_delete_user["email"],
            "password": user_data_with_delete_user["password"],
            "name": f'{user_data_with_delete_user["name"]}test'
        }
        response = requests.patch(Urls.url_user_change_data, json=payload)
        assert response.status_code == 401
        assert response.json()["message"] == no_auth