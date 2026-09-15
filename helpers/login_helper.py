# helpers/login_helper.py

import requests
from urls import AUTH


class LoginHelper:

    @staticmethod
    def login_user(email, password):
        payload = { "email": email,"password": password,}
        response = requests.post(AUTH["login"], json=payload)  
        return response     
