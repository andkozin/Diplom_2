# urls.py

BASE_URL = "https://stellarburgers.education-services.ru"

AUTH = {
    "register": f"{BASE_URL}/api/auth/register",
    "login": f"{BASE_URL}/api/auth/login",
    "user": f"{BASE_URL}/api/auth/user",  # DELETE и GET
        }

INGREDIENTS = {
    "list": f"{BASE_URL}/api/ingredients",
    }

ORDERS = {
    "create": f"{BASE_URL}/api/orders",
    "list": f"{BASE_URL}/api/orders",
    }