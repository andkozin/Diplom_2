# helpers/login_helper.py

import allure
import requests
from urls import AUTH
from helpers.allure_helper import attach_api_call


class LoginHelper:

    @staticmethod
    @allure.step("Выполняем логин пользователя: email={email}, password={password}")
    def login_user(email, password):
        payload = { "email": email,"password": password,}
        response = requests.post(AUTH["login"], json=payload) 
        attach_api_call(payload, response, AUTH["login"], prefix="Login") 
        return response     
