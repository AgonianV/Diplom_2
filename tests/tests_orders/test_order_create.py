import allure
import requests
from conftest import user_data_with_delete_user
from src.urls import Urls
from src.messages import *
from src.data import *

class TestOrderCreate:

    def test_create_order_without_login(self):
        payload = {"ingredients": "61c0c5a71d1f82001bdaaa6e"}
        responce = requests.post(Urls.url_order_create, json=payload)
        assert responce.status_code == 200
        assert responce.json()["name"] == "Люминесцентный бургер"



    def test_create_order_without_ingredients(self):
        payload = {"ingredients": ""}
        responce = requests.post(Urls.url_order_create, json=payload)
        assert responce.status_code == 400
        assert responce.json()["message"] == no_ingredients