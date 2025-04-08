import requests
import json
from API.payloads import AuthorizationPayload2 
from dotenv import load_dotenv
import os

load_dotenv()


 # convert to process env
BASE_URL = os.getenv("BASE_URL")
CHECK_AND_SEND = BASE_URL + "/auth/email/check-and-send"
SIGN_IN = BASE_URL + "/auth/sign-in"
auth = AuthorizationPayload2



class Authorization():
    def __init__(self):
        self.refresh_token = None
        self.auth_token = None

    def get_refresh_and_auth_token(self):
        """ Получение refresh_token для пользователя и запись в переменную """

        response = requests.post(CHECK_AND_SEND, json=auth.check_and_send_payload)
        assert response.status_code == 200, "Ошибка в check-and-send запросе"

        headers = {"Device-id": os.getenv("device_id_second")}
        response = requests.post(SIGN_IN, json=auth.sign_in, headers=headers)
        assert response.status_code == 200, "Ошибка в sign-in запросе"

        self.refresh_token = response.json().get("meta", {}).get("refreshToken")
        
        """ Получение auth_token для пользователя и запись в переменную """
        response = requests.post(CHECK_AND_SEND, json=auth.check_and_send_payload)
        assert response.status_code == 200, "Ошибка в check-and-send запросе"

        headers = {"Device-id": os.getenv("device_id_second")}
        response = requests.post(SIGN_IN, json=auth.sign_in, headers=headers)
        assert response.status_code == 200, "Ошибка в sign-in запросе"

        self.auth_token = response.json().get("meta", {}).get("authToken")
        return self.auth_token
    