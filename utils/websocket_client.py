import socketio
import json
from datetime import datetime
from API.payloads import AuthorizationPayloadReceiver
from utils.logger import Logger
from API.api_auth import AuthorizationApi
import os
from dotenv import load_dotenv

load_dotenv(".env.dev")


sio = socketio.Client()
logger = Logger()


BASE_URL = os.getenv("BASE_URL_API")
CHECK_AND_SEND = BASE_URL + "/auth/email/check-and-send"
SIGN_IN = BASE_URL + "/auth/sign-in"

class WebSocket(AuthorizationApi):
    def __init__(self):
        super().__init__()

    @sio.on("*") 
    def catch_all(event, data):
        print(f"\n EVENT: {event}")
        print(f" DATA: {data}")

    @sio.on('USER_TYPING')
    def handle_user_typing(data):
        print(f"\nUSER TYPING IN CHANNEL, CHANNEL ID: {data.get('channelId')}")
    
    @sio.on("ACTION__CROSS_WORKSPACE_NOTIFIER")
    def handle_cheto_tam(event, data):
        print(f"\n EVENT: {event}")
        print(f" DATA: {data}")

    @sio.on("CHAT__READ_MESSAGES_STATUS_SYNC") 
    def handle_chat_read_messages_status_sync(data):
        print("\n EVENT: CHAT__READ_MESSAGES_STATUS_SYNC")
        print(" DATA:")
        print(json.dumps(data, indent=2, ensure_ascii=False))


    def tokens(self):
        self.get_refresh_token()
        self.get_auth_token()

    def connect_websocket_with_user(self, auth):
        """Подключение к WebSocket"""
        self.set_auth(auth)
        self.tokens()
        logger.info("Получение Токенов...")
        logger.info(f"{self.auth_token} <<<< AuthToken")
        logger.info(f"{self.refresh_token} <<< RefreshToken")
        logger.info('Connect to WebSocket...')

        try:
            sio.connect(
                "https://api.dev.sphera.work/api/v1",
                transports=['websocket'],
                auth={
                    'auth_token': self.auth_token,
                    'token': self.refresh_token,
                    'deviceId': config.get("DEVICE_ID_SECOND"),
                    'activeCompanies': '[]'
                }
            )
            logger.info(f"Состояние подключения: {sio.connected}")
            logger.info(f"ID сессии: {sio.sid}")
            logger.info("Успешно подключились к WebSocket!")
        except Exception as e:
            logger.error(f"Ошибка подключения к WebSocket: {e}")
        except ConnectionRefusedError as e:
            logger.error(f"Сервер отклонил подключение: {e}")
        except ConnectionResetError as e:
            logger.error(f"Сервер разорвал соединение: {e}")

    def disconnect_websocket(self):
        """Отключение от WebSocket"""
        try:
            if sio.connected:
                sio.disconnect()
                logger.info("WebSocket корректно отключен")
            else:
                logger.error("Попытка отключения неактивного соединения WebSocket")
                
        except ConnectionAbortedError as e:
            logger.error(f"Соединение было уже разорвано: {e}")



    # Работают после создания канала ;(

    # EVENT: NEW_ACTION_MESSAGE
    # CHAT__NEW_MESSAGE
    # CHAT__REACTION_UPDATED
    # MESSAGE_DELETED
    # GET_UPDATED_MESSAGE