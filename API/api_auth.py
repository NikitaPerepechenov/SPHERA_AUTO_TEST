import requests
import json
from API.payloads import AuthorizationPayload as auth

BASE_URL = "https://api.dev.sphera.work/api/v1"
CHECK_AND_SEND = BASE_URL + "/auth/email/check-and-send"
SIGN_IN = BASE_URL + "/auth/sign-in"
DEVICE_ID_FIRST_USER = "a8100b26-82e7-427e-b731-9ccbabcf62f5"
DEVICE_ID_SECOND_USER = "f6b7dbc5-7cc6-4905-928a-e9a57fa2abcb"

headers = {
    "Content-Type": "application/json",
    "Device-id": DEVICE_ID_FIRST_USER 
}

class Authorization:
    def get_refresh_token_first_user(self):
        """ Получение refresh_token для первого пользователя и запись в переменную """

        response = requests.post(CHECK_AND_SEND, json=auth.check_and_send_payload)
        assert response.status_code == 200, "Ошибка в check-and-send запросе"

        headers = {"Device-id": DEVICE_ID_FIRST_USER}
        response = requests.post(SIGN_IN, json=auth.sign_in, headers=headers)
        assert response.status_code == 200, "Ошибка в sign-in запросе"

        self.refresh_token = response.json().get("meta", {}).get("refreshToken")
        return self.refresh_token
    
    def get_refresh_token_second_user(self):
        """ Получение refresh_token для второго пользователя и запись в переменную """

        response = requests.post(CHECK_AND_SEND, json=auth.check_and_send_payload)
        assert response.status_code == 200, "Ошибка в check-and-send запросе"

        headers = {"Device-id": DEVICE_ID_SECOND_USER}
        response = requests.post(SIGN_IN, json=auth.sign_in, headers=headers)
        assert response.status_code == 200, "Ошибка в sign-in запросе"

        self.refresh_token = response.json().get("meta", {}).get("refreshToken")
        return self.refresh_token
    
    
    def get_auth_token_first_user(self):
        """ Получение auth_token для первого пользователя и запись в переменную """
        response = requests.post(CHECK_AND_SEND, json=auth.check_and_send_payload)
        assert response.status_code == 200, "Ошибка в check-and-send запросе"

        headers = {"Device-id": DEVICE_ID_FIRST_USER}
        response = requests.post(SIGN_IN, json=auth.sign_in, headers=headers)
        assert response.status_code == 200, "Ошибка в sign-in запросе"

        self.auth_token = response.json().get("meta", {}).get("authToken")
        return self.auth_token
    
    def get_auth_token_second_user(self):
        """ Получение auth_token для второго пользователя и запись в переменную """
        response = requests.post(CHECK_AND_SEND, json=auth.check_and_send_payload)
        assert response.status_code == 200, "Ошибка в check-and-send запросе"

        headers = {"Device-id": DEVICE_ID_SECOND_USER}
        response = requests.post(SIGN_IN, json=auth.sign_in, headers=headers)
        assert response.status_code == 200, "Ошибка в sign-in запросе"

        self.auth_token = response.json().get("meta", {}).get("authToken")
        return self.auth_token
    


