from src.helpers import generate_random_string

def generate_user_data():
    email = generate_random_string(10)
    password = generate_random_string(10)
    name = generate_random_string(10)

    return {
        "email": f"{email}@yandex.ru",
        "password": password,
        "name": name
    }