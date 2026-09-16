# helpers/order_helper.py
import allure

import requests
from urls import INGREDIENTS, ORDERS
from helpers.allure_helper import attach_api_call


class OrderHelper:

#/api/orders — создание заказа
    @staticmethod
    @allure.step("Создаём заказ (с авторизацией) access_token={access_token}")
    # @allure.step("Создаём заказ: ingredients={ingredients}, access_token={access_token}")
    def create_order(ingredients, access_token=None):
    
        payload = {"ingredients": ingredients}
        headers = {}
        if access_token:
            headers["Authorization"] = access_token

        response = requests.post(ORDERS["create"], json=payload, headers=headers)
        attach_api_call(payload, response, ORDERS["create"], prefix="CreateOrder")
        return response


#/api/ingredients - получил и булку и ингридиент
    @staticmethod
    @allure.step("Получаем ID булочки и основных ингредиентов")
    def get_bun_and_main_ids():
        
        response = requests.get(INGREDIENTS["list"])
        attach_api_call(None, response, INGREDIENTS["list"], prefix="GetIngredients")

        data = response.json().get("data", [])

        for item in data:
            if item.get("type") == "bun":
                bun = item

        for item in data:
            if item.get("type") == "main":
                main = item
    
        return [bun["_id"], main["_id"]]
