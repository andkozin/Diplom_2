# conftest.py

import pytest
from helpers.user_helper import UserHelper
from helpers.login_helper import LoginHelper
from helpers.order_helper import OrderHelper
from helpers.data_generator import get_user_payload


@pytest.fixture
def user_helper():
    return UserHelper()


@pytest.fixture
def login_helper():
    return LoginHelper()

@pytest.fixture # тест созд. пользов. и передал фикстуре токен для удаления
def user_cleanup(user_helper):
    
    tokens = []

    def register(token):
        if token:
            tokens.append(token)

    yield register

    for token in tokens:
        user_helper.delete_user(token)

@pytest.fixture
def registered_user(user_helper):
    payload = get_user_payload()

    access_token = user_helper.create_and_get_token(
        payload["email"],
        payload["password"],
        payload["name"]
    )

    yield {
        "email": payload["email"],
        "password": payload["password"],
        "name": payload["name"],
        "access_token": access_token,
    }

    user_helper.delete_user(access_token)
    

@pytest.fixture
def order_helper():
    return OrderHelper()

@pytest.fixture
def ingredient_hashes(order_helper):
    return order_helper.get_bun_and_main_ids()

