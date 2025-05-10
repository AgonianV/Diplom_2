
import allure
import requests
from conftest import user_data_new_with_delete, user_data_with_delete_user
from src.urls import Urls
from src.messages import *
from src.data import *

class TestUserCreate:

    @allure.title('Cоздание уникального юзера')
    def test_create_new_user(self, user_data_new_with_delete):

        assert user_data_new_with_delete.status_code == 200



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

    @allure.title("Создание без без обязательного поля") # ответ на запрос не соответствует документации
    def test_create_user_password_is_empty(self, user_data_new):
        user_data_new.pop("password")
        response = requests.post(Urls.url_user_create, json=user_data_new)
        assert response.status_code == 403
        assert response.json()["message"] == empty_required_field