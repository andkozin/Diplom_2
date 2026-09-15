import requests
from urls import AUTH


class UserHelper:

   
#/api/auth/register-создание уник. польз. 
    @staticmethod
    def create_user( email, password, name):
        payload = {"email": email, "password": password, "name": name}

        response = requests.post(url=AUTH["register"],json=payload,) # попробывать через session
        return response

    @staticmethod
    def create_and_get_token(email, password, name):
        response = UserHelper.create_user(email, password, name)
        return response.json().get("accessToken", "")


#/api/auth/user-удаление пользователя
    @staticmethod
    def delete_user(access_token) :
        headers = {"Authorization": access_token}

        response = requests.delete(url=AUTH["user"],headers=headers,)
        return response

