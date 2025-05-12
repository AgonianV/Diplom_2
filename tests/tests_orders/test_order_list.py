import allure
import requests
from conftest import user_data_with_delete_user
from src.urls import Urls
from src.messages import *
from src.data import *

class TestGetOrderList:
    @allure.title("Получение списка заказов с авторизованного пользователя")
    def test_get_order_list_login_user(self, user_data_with_delete_user):
        payload = {"ingredients": "61c0c5a71d1f82001bdaaa6e"}
        headers = {"Authorization": user_data_with_delete_user["token"]}
        for i in range(3):
            response = requests.post(Urls.url_order_create,headers=headers, json=payload)
        get_response = requests.get(Urls.url_order_create,headers=headers)
        assert get_response.status_code == 200
        assert len(get_response.json()["orders"]) == 3

    @allure.title("Получение списка заказов с неавторизованного пользователя")
    def test_get_order_list_no_login_user(self):
        payload = {"ingredients": "61c0c5a71d1f82001bdaaa6e"}
        for i in range(2):
            response = requests.post(Urls.url_order_create, json=payload)
        get_response = requests.get(Urls.url_order_create)
        assert get_response.status_code == 401
        assert get_response.json()["message"] == no_auth