# tests/test_login_user.py
import allure
import data
from helpers.data_generator import get_user_payload

@allure.feature("Логин пользователя - Stellar Burgers API")
class TestLoginUser:

    @allure.title("Вход с существующим пользователем")
    def test_login_create_user(self, login_helper, registered_user):
        
        with allure.step("Запрос на вход с существующим пользователем"):
            payload = {
                "email": registered_user["email"],
                "password": registered_user["password"],
}
            
            response = login_helper.login_user(
                registered_user["email"], registered_user["password"]
            )

        assert response.status_code == data.STATUS_OK
        assert response.json()["success"] is data.MSG_SUCCESS_TRUE
        assert "accessToken" in response.json(), "В ответе отсутствует accessToken"
        assert "refreshToken" in response.json(), "В ответе отсутствует refreshToken"

    @allure.title("Вход с неверным паролем")
    def test_login_invalid_password(self, login_helper, registered_user):
        payload = {
        "email": registered_user["email"],
        "password": "invalid_pass",  
    }
        with allure.step("Отправить запрос с неверным паролем"):

            response = login_helper.login_user(payload["email"], payload["password"])
           
        assert response.status_code == data.STATUS_401_UNAUTHORIZED
        assert response.json()["success"] is data.MSG_SUCCESS_FALSE
        assert data.MSG_INVALID_CREDENTIALS in response.json()["message"]


    @allure.title("Вход с несущест.  email") # сделал без регистраци -пользователя вообще нет
    def test_login_nonexistent_user(self, login_helper):
        payload = get_user_payload()

        with allure.step("Запрос с несущест. email"):
            response = login_helper.login_user(payload["email"], payload["password"])

        assert response.status_code == data.STATUS_401_UNAUTHORIZED
        assert response.json()["success"]  is data.MSG_SUCCESS_FALSE
        assert data.MSG_INVALID_CREDENTIALS in response.json()["message"]
