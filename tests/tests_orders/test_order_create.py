import allure
import requests
from conftest import user_data_with_delete_user
from src.urls import Urls
from src.messages import *
from src.data.ingredient_data import Ingredients


class TestOrderCreate:
    @allure.title("Создание заказа с одним ингредиентом с неавторизованного пользователя")
    def test_create_order_without_login(self):
        responce = requests.post(Urls.url_order_create, json=Ingredients.one_correct_ingredients_data)
        assert responce.status_code == 200
        assert responce.json()["name"] == "Люминесцентный бургер"

    @allure.title("Создание заказа с несколькими ингредиентами с неавторизованного пользователя")
    def test_create_order_without_login_two_ingredients(self):
        responce = requests.post(Urls.url_order_create, json=Ingredients.two_correct_ingredients_data)
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
        responce = requests.post(Urls.url_order_create, json=Ingredients.one_incorrect_ingredients_data)
        assert responce.status_code == 500

    @allure.title("Создание заказа с одним ингредиентом с авторизованного пользователя")
    def test_create_order_with_login_user(self, user_data_with_delete_user):
        headers = {"Authorization": user_data_with_delete_user["token"]}
        response = requests.post(Urls.url_order_create,headers=headers, json=Ingredients.one_correct_ingredients_data)
        assert response.status_code == 200
        assert response.json()["order"]["owner"]["email"] == user_data_with_delete_user["email"]

    @allure.title("Создание заказа с несколькими ингредиентами с авторизованного пользователя")
    def test_create_order_with_login_user_two_ingredients(self, user_data_with_delete_user):
        headers = {"Authorization": user_data_with_delete_user["token"]}
        response = requests.post(Urls.url_order_create,headers=headers, json=Ingredients.two_correct_ingredients_data)
        assert response.status_code == 200
        assert response.json()["order"]["price"] == 5130

    