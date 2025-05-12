import allure
import requests
from conftest import user_data_with_delete_user
from src.urls import Urls
from src.messages import *
from src.data import *

class TestOrderCreate:
    @allure.title("Создание заказа с одни ингредиентом с неавторизованного пользователя")
    def test_create_order_without_login(self):
        payload = {"ingredients": "61c0c5a71d1f82001bdaaa6e"}
        responce = requests.post(Urls.url_order_create, json=payload)
        assert responce.status_code == 200
        assert responce.json()["name"] == "Люминесцентный бургер"

    @allure.title("Создание заказа с несколькими ингредиентами с неавторизованного пользователя")
    def test_create_order_without_login_two_ingredients(self):
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6e", "61c0c5a71d1f82001bdaaa7a"]}
        responce = requests.post(Urls.url_order_create, json=payload)
        assert responce.status_code == 200
        assert responce.json()["name"] == "Люминесцентный астероидный бургер"

    @allure.title("Создание заказа без ингредиентов с неавторизованного пользователя")
    def test_create_order_without_ingredients(self):
        payload = {"ingredients": ""}
        responce = requests.post(Urls.url_order_create, json=payload)
        assert responce.status_code == 400
        assert responce.json()["message"] == no_ingredients

    @allure.title("Создание заказа с некорректным хешем ингредиента")
    def test_create_order_with_incorrect_hash(self):
        payload = {"ingredients": "609646e4dc916e00276b28702"}
        responce = requests.post(Urls.url_order_create, json=payload)
        assert responce.status_code == 500

    @allure.title("Создание заказа с одни ингредиентом с авторизованного пользователя")
    def test_create_order_with_login_user(self, user_data_with_delete_user):
        payload = {"ingredients": "61c0c5a71d1f82001bdaaa6e"}
        headers = {"Authorization": user_data_with_delete_user["token"]}
        response = requests.post(Urls.url_order_create,headers=headers, json=payload)
        assert response.status_code == 200
        assert response.json()["order"]["owner"]["email"] == user_data_with_delete_user["email"]

    @allure.title("Создание заказа с несколькими ингредиентами с авторизованного пользователя")
    def test_create_order_with_login_user_two_ingredients(self, user_data_with_delete_user):
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6e", "61c0c5a71d1f82001bdaaa7a"]}
        headers = {"Authorization": user_data_with_delete_user["token"]}
        response = requests.post(Urls.url_order_create,headers=headers, json=payload)
        assert response.status_code == 200
        assert response.json()["order"]["price"] == 5130

    