import random
import requests
import string
from src.urls import Urls
from faker import Faker
import allure

fake = Faker('ru_RU')

@allure.step('Удаление юзера')
def delete_user(email, token):
    payload = {"email": email}
    headers = {"Authorization": token}
    response = requests.delete(Urls.url_user_delete, headers=headers, json=payload)
    return response

@allure.step('Генерация строки')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@allure.step('Генерация данных для пользователя')
def generate_user_data():
    email = generate_random_string(10)
    password = generate_random_string(10)
    username = generate_random_string(10)

    return {
            "email": f"{email}@yandex.ru",
            "password": password,
            "name": username
            }


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@allure.step('метод регистрации нового курьера')
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(Urls.url_order_create, data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass

@allure.step('Загрузка данных заказа')
def order_data():
    payload_order = {
        "firstName": fake.first_name_male(),
        "lastName": fake.last_name_male(),
        "address": "Санкт-Петербург, Невский проспект 24",
        "metroStation": 2,
        "phone": "+7 921 335 39 13 ",
        "rentTime": 5,
        "deliveryDate": str(fake.future_date()),
        "comment": "Добрый вечер",
        "color": ["BLACK"]
    }
    return payload_order
