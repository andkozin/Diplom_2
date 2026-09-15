import requests
from urls import INGREDIENTS, ORDERS


class OrderHelper:

#/api/orders — создание заказа
    @staticmethod
    def create_order(ingredients, access_token=None):
    
        payload = {"ingredients": ingredients}
        headers = {}
        if access_token:
            headers["Authorization"] = access_token

        response = requests.post(ORDERS["create"], json=payload, headers=headers)
        return response


#/api/ingredients - получил и булку и ингридиент
    @staticmethod
    def get_bun_and_main_ids():
        
        response = requests.get(INGREDIENTS["list"])
        data = response.json().get("data", [])

        for item in data:
            if item.get("type") == "bun":
                bun = item

        for item in data:
            if item.get("type") == "main":
                main = item
    
        return [bun["_id"], main["_id"]]
