import pytest
from src.data import *



@pytest.fixture
def user_data_new():
    payload = generate_user_data()
    yield payload






