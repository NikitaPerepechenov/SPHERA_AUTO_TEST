import requests
import json
from payloads import AuthorizationPayload as auth

BASE_URL = "https://api.dev.sphera.work/api/v1/"
CHECK_AND_SEND = BASE_URL + "auth/email/check-and-send"
SIGN_IN = BASE_URL + "auth/sign-in"

headers = {
    "Content-Type": "application/json",
    "Device-id": "a8100b26-82e7-427e-b731-9ccbabcf62f5" 
}

class Authorization:
    def get_refresh_token(self):
        """ Получение refresh_token и запись в переменную """

        response = requests.post(CHECK_AND_SEND, json=auth.check_and_send_payload)
        assert response.status_code == 200, "Ошибка в check-and-send запросе"

        headers = {"Device-id": "a8100b26-82e7-427e-b731-9ccbabcf62f5"}
        response = requests.post(SIGN_IN, json=auth.sign_in, headers=headers)
        assert response.status_code == 200, "Ошибка в sign-in запросе"

        self.refresh_token = response.json()["meta"]["refreshToken"]
        return self.refresh_token