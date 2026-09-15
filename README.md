# Diplom_2 — автотесты для Stellar Burgers (API)

Автотесты на Python: pytest + requests (API) + Allure.

## Покрытие API-тестов (по заданию)

Все кейсы из задания реализованы в отдельных классах с Allure-разметкой и прикреплением запросов/ответов.

### Создание пользователя

| Кейс | Реализация | Особенности |
| --- | --- | --- |
| Позитивный: уникальный пользователь | TestCreateUser.test_create_unique_user | После теста пользователь удаляется через delete_user — обеспечена атомарность тестов. |
| Негативный: дубликат пользователя | TestCreateUser.test_create_duplicate_user | Проверка статуса 403 Forbidden и сообщения MSG_USER_ALREADY_EXISTS. |
| Негативный: пропуск обязательного поля | TestCreateUser.test_create_user_missing_field | Параметризация по полям email/password/name. Проверка статуса 403 и сообщения MSG_EMAIL_PASSWORD_REQUIRED. |

### Логин пользователя

| Кейс | Реализация | Особенности |
| --- | --- | --- |
| Позитивный: успешный вход | TestLoginUser.test_login_create_user | Получение accessToken и refreshToken, проверка success=true. |
| Негативный: неверный пароль | TestLoginUser.test_login_invalid_password | Статус 401 Unauthorized, сообщение MSG_INVALID_CREDENTIALS. |
| Негативный: несуществующий email | TestLoginUser.test_login_nonexistent_user | Статус 401 Unauthorized, проверка сообщения об ошибке. |

### Создание заказа

| Кейс | Реализация | Особенности |
| --- | --- | --- |
| Позитивный: заказ с авторизацией и ингредиентами | TestCreateOrder.test_create_order_with_auth | Проверка статуса 200, success=true, наличие поля order.number. |
| Негативный: заказ без авторизации | TestCreateOrder.test_create_order_without_auth | В текущей реализации ожидается статус 200 и success=true. Если по ТЗ создание заказа без авторизации должно быть запрещено, тест требуется скорректировать. |
| Негативный: заказ без ингредиентов | TestCreateOrder.test_create_order_without_ingredients | Проверка статуса 400 Bad Request и сообщения MSG_INGREDIENTS_REQUIRED. |
| Негативный: неверный хеш ингредиентов | TestCreateOrder.test_create_order_with_invalid_hash | Проверка статуса 500 Internal Server Error. |



## Как запустить тесты

rm -rf allure-results/

pytest tests/ -v --alluredir=allure-results

allure serve allure-results

zip -r allure-results.zip allure-results/