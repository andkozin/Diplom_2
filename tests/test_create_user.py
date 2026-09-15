import allure
import pytest
import data
from helpers.data_generator import get_user_payload, modify_payload_for_field
from helpers.allure_helper import attach_api_call


@allure.feature("Создание пользователя - Stellar Burgers API")
class TestCreateUser:

    @allure.title("Создание уник. пользователя")
    def test_create_unique_user(self, user_helper):
        payload = get_user_payload()

        with allure.step("Запрос на созд. пользователя"):
            
            response = user_helper.create_user(
                payload["email"], payload["password"], payload["name"]
            )
            attach_api_call(payload, response, response.url, prefix="Уник.польз.")

        with allure.step(f"Проверит код ({data.STATUS_OK})"):
            assert response.status_code == data.STATUS_OK

        with allure.step("Проверка success = true"):
            assert response.json()["success"] is data.MSG_SUCCESS_TRUE

        with allure.step("Проверка accessToken и refreshToken"):
            assert "accessToken" in response.json()
            assert "refreshToken" in response.json()

        # удаление аользователя
        access_token = response.json().get("accessToken")
        user_helper.delete_user(access_token)

    @allure.title("Создание пользователя, который уже создан")
    def test_create_duplicate_user(self, user_helper, registered_user):
        payload = {
            "email": registered_user["email"],
            "password": registered_user["password"],
            "name": registered_user["name"],
        }
            
        with allure.step("Запрос на созд. пользователя - уже создан"):
            allure.attach(
                           name="Уже создан",
                           body=str(payload),
                           attachment_type=allure.attachment_type.TEXT,)
            
            response = user_helper.create_user(
                payload["email"], payload["password"], payload["name"]
            )
            attach_api_call(payload, response, response.url, prefix="Уже создан")

        with allure.step(f"Проверить статус-код ({data.STATUS_403_FORBIDDEN})"):
            assert response.status_code == data.STATUS_403_FORBIDDEN

        with allure.step("Проверка сообщение об ошибке"):   
            json = response.json()
            assert json.get("success") is data.MSG_SUCCESS_FALSE
            assert data.MSG_USER_ALREADY_EXISTS in response.json()["message"]



    @pytest.mark.parametrize(
        "field_to_remove",
        ["email", "password", "name"],
        ids=["без email", "без password", "без name"],
    )
    @allure.title("Создание пользователя без обязательного поля: {field_to_remove}")
    def test_create_user_missing_field(self, user_helper, field_to_remove):
        base = get_user_payload()
        payload = modify_payload_for_field(base, field_to_remove, None)

        with allure.step(f"Отправить запрос без поля {field_to_remove}"):
            
            response = user_helper.create_user(
                payload.get("email", ""),
                payload.get("password", ""),
                payload.get("name", ""),
            )
            attach_api_call(payload, response, response.url, prefix=f"Без поля {field_to_remove.capitalize()}")


        with allure.step(f"Проверить статус-код ({data.STATUS_403_FORBIDDEN})"):
            assert response.status_code == data.STATUS_403_FORBIDDEN

        with allure.step("Проверить сообщение об ошибке"):
            json = response.json()
            assert json.get("success") is data.MSG_SUCCESS_FALSE
            # assert response.json()["success"] is False
            assert data.MSG_EMAIL_PASSWORD_REQUIRED in response.json()["message"]
