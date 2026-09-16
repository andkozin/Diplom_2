# tests/test_create_order.py
import allure
import pytest
from helpers.allure_helper import attach_api_call
import data

@allure.feature("Создание заказа- Stellar Burgers API")
class TestCreateOrder:

    @allure.title("Создание заказа с логином и сущест. ингредиентами")
    def test_create_order_with_auth(self, order_helper, registered_user, ingredient_hashes):
        with allure.step("Запрос на создание заказа с логином"):
            response = order_helper.create_order(
                ingredient_hashes, access_token=registered_user["access_token"]
            )

            attach_api_call(
                payload={"ingredients": ingredient_hashes},
                response=response,
                url=response.url,
                prefix="Создание с логином",
                )

        with allure.step(f"Проверить статус-код ({data.STATUS_OK})"):
            assert response.status_code == data.STATUS_OK

        with allure.step("Проверить success = true"):
            assert response.json()["success"] is data.MSG_SUCCESS_TRUE

        assert "order" in response.json() and "number" in response.json()["order"], \
        "Не получен номер заказа"
        


    @allure.title("Создание заказа без логина")
    def test_create_order_without_auth(self, order_helper, ingredient_hashes):
        with allure.step("Запрос без токена"):
            response = order_helper.create_order(ingredient_hashes, access_token=None)

            attach_api_call(
                payload={"ingredients": ingredient_hashes},
                response=response,
                url=response.url,
                prefix="Создание без логина",
            )
        with allure.step(f"Проверить статус-код ({data.STATUS_OK})"):
            assert response.status_code == data.STATUS_OK
        
        with allure.step("Проверить success = true"):
            assert response.json()["success"] is data.MSG_SUCCESS_TRUE
        
        assert "order" in response.json() and "number" in response.json()["order"], \
                "Не получен номер заказа"
    

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, order_helper, registered_user):
        with allure.step("Запрос без ингредиентов"):
            response = order_helper.create_order(
                [], access_token=registered_user["access_token"]
            )

            attach_api_call(
                payload={"ingredients": []},
                response=response,
                url=response.url,
                prefix="Без ингридиентов",
                )

        with allure.step(f"Проверить код ({data.STATUS_400_BAD_REQUEST})"):
            assert response.status_code == data.STATUS_400_BAD_REQUEST

        assert response.json()["success"] is False
        assert data.MSG_INGREDIENTS_REQUIRED in response.json()["message"]



    @allure.title("Создание заказа с неверным хешем")
    def test_create_order_with_invalid_hash(self, order_helper, registered_user):
        invalid_hash = "123456"
        payload = {"ingredients": [invalid_hash]}

        with allure.step("Отправить запрос с неверным хешем"):
            response = order_helper.create_order(
                [invalid_hash], access_token=registered_user["access_token"]
            )
            attach_api_call(
                payload=payload,
                response=response,
                url=response.url,
                prefix="Неверный хэш",
            )

        assert response.status_code == data.STATUS_500_INTERNAL_SERVER_ERROR
