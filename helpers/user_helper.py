# helpers/user_helper.py
import allure

import helpers
import requests
from urls import AUTH
from helpers.allure_helper import attach_api_call


class UserHelper:

   
#/api/auth/register-создание уник. польз. 
    @staticmethod
    @allure.step("Регистрируем пользователя: email={email}, name={name}")
    def create_user( email, password, name):
        payload = {"email": email, "password": password, "name": name}

        response = requests.post(url=AUTH["register"],json=payload,) # попробывать через session
        attach_api_call(payload, response, AUTH["register"], prefix="RegisterUser")
        return response

    @staticmethod
    @allure.step("Регистрируем и получаем токен: email={email}, name={name}")
    def create_and_get_token(email, password, name):
        response = UserHelper.create_user(email, password, name)
        return response.json().get("accessToken", "")


#/api/auth/user-удаление пользователя
    @staticmethod
    @allure.step("Удаляем пользователя по токену")
    def delete_user(access_token) :
        headers = {"Authorization": access_token}

        response = requests.delete(url=AUTH["user"],headers=headers,)
        attach_api_call(None, response, AUTH["user"], prefix="DeleteUser")
        return response

