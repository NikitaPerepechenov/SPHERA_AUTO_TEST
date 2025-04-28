import requests
import json
from dotenv import load_dotenv
import os

load_dotenv(".env.dev")


BASE_URL = os.getenv("BASE_URL_API")
CHECK_AND_SEND = BASE_URL + "/auth/email/check-and-send"
SIGN_IN = BASE_URL + "/auth/sign-in"

class AuthorizationApi():
    auth: None

    def set_auth(self, auth):
        self.auth = auth

    def get_refresh_token(self):
        """ Получение refresh_token для пользователя и запись в переменную """

        response = requests.post(CHECK_AND_SEND, json=self.auth.check_and_send_payload)
        assert response.status_code == 200, "Ошибка в check-and-send запросе"

        headers = {"Device-id": os.getenv("DEVICE_ID_SECOND")}
        response = requests.post(SIGN_IN, json=self.auth.sign_in, headers=headers)
        assert response.status_code == 200, "Ошибка в sign-in запросе"

        self.refresh_token = response.json().get("meta", {}).get("refreshToken")
        return self.refresh_token
        
    def get_auth_token(self):
        """ Получение auth_token для пользователя и запись в переменную """

        response = requests.post(CHECK_AND_SEND, json=self.auth.check_and_send_payload)
        assert response.status_code == 200, "Ошибка в check-and-send запросе"

        headers = {"Device-id": os.getenv("DEVICE_ID_SECOND")}
        response = requests.post(SIGN_IN, json=self.auth.sign_in, headers=headers)
        assert response.status_code == 200, "Ошибка в sign-in запросе"

        self.auth_token = response.json().get("meta", {}).get("authToken")
        return self.auth_token