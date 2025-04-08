import socketio
import json
from datetime import datetime
from utils.logger import Logger
from dotenv import load_dotenv
from API.api_auth import Authorization
import os


load_dotenv()

sio = socketio.Client()
logger = Logger()


BASE_URL = os.getenv("BASE_URL")
CHECK_AND_SEND = BASE_URL + "/auth/email/check-and-send"
SIGN_IN = BASE_URL + "/auth/sign-in"

class WebSocket(Authorization):
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
        self.get_refresh_and_auth_token()

    def connect_websocket_with_user(self):
        """Подключение к WebSocket"""
        self.tokens()
        logger.info("Получение Токенов...")
        logger.info(f"{self.auth_token} <<<< AuthToken")
        logger.info(f"{self.refresh_token} <<< RefreshToken")
        logger.info('Connect to WebSocket...')

        try:
            sio.connect(
                os.getenv("WEBSOCKET_DEV"),
                transports=['websocket'],
                auth={
                    'auth_token': self.auth_token,
                    'token': self.refresh_token,
                    'deviceId': os.getenv("DEVICE_ID_SECOND"),
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