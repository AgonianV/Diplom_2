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
    requests.delete(Urls.url_user_delete, headers=headers, json=payload)


@allure.step('Генерация строки')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@allure.step('Генерация данных для пользователя')
def generate_user_data():
    email = generate_random_string(10)
    password = generate_random_string(10)
    name = generate_random_string(10)

    return {
            "email": f"{email}@yandex.ru",
            "password": password,
            "name": name
            }


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@allure.step('метод регистрации нового пользователя')
def register_new_user_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    email = generate_random_string(10)
    password = generate_random_string(10)
    name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "email": f"{email}@yandex.ru",
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(Urls.url_user_create, data=payload)
    response_data = response.json()
    # если регистрация прошла успешно (код ответа 200), добавляем в список логин и пароль юзера
    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(name)
        login_pass.append(response_data["accessToken"])
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
