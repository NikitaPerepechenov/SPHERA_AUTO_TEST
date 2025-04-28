import socketio
import json
import os 
from dotenv import load_dotenv
from datetime import datetime
from utils.logger import Logger
from API.api_auth import Authorization

load_dotenv()
sio = socketio.Client()
logger = Logger()


BASE_URL = os.getenv("BASE_URL_API")
CHECK_AND_SEND = BASE_URL + "/auth/email/check-and-send"
SIGN_IN = BASE_URL + "/auth/sign-in"
DEVICE_ID_FIRST_USER = os.getenv("DEVICE_ID_FIRST")
DEVICE_ID_SECOND_USER = os.getenv("DEVICE_ID_SECOND")
class WebSocket(Authorization):
    def __init__(self):
        super().__init__()
        api = Authorization()
        self.refresh_token_first_user = api.get_refresh_token_first_user()
        self.auth_token_first_user = api.get_auth_token_first_user()

        self.refresh_token_second_user = api.get_refresh_token_second_user()
        self.auth_token_second_user = api.get_auth_token_second_user()

        
    @sio.on('*')
    def catch_all(event, data):
        print(f"\n[RAW EVENT] {event}:")
        print(json.dumps(data, indent=2, ensure_ascii=False))

    @sio.on('ADD_USERS_TO_CHANNEL')
    def handle_add_user_to_channel(data):
        print(f"\n ADD USER(S) TO CHANNEL : {data.get('channelId')}")
        users = []
        if 'users' in data:
            users = data['users']
        elif 'userToChannels' in data:
            users = [item['user'] for item in data['userToChannels'] if 'user' in item]
        
        for user in users:
            name = f"{user.get('firstName', '')} {user.get('lastName', '')}".strip()
            print(f"Пользователь: {name} (ID: {user.get('userId')})")

    @sio.on('USER_TYPING')
    def handle_user_typing(data):
        print(f"\nUSER TYPING IN CHANNEL, CHANNEL ID: {data.get('channelId')}")

    @sio.on('MESSAGE_DELETED')
    def handle_message_deleted(data):
        print("\n[MESSAGE_DELETED] Сообщение удалено:")
        print(f"Message ID: {data.get('messageId')}")
        print(f"Channel: {data.get('channelId')}")
        print(f"Deleted at: {data.get('deletedAt')}")
        print(f"Received at: {datetime.now().strftime('%H:%M:%S')}")

    @sio.on('DELETED_CHANNEL')
    def handle_channel_deleted(data):
        print("\n[CHANNEL DELETED] Канал удален:")
        print(f"Channel ID: {data.get('channelId')}")
        print("Full data:", json.dumps(data, indent=2))

    @sio.on('UNARCHIVED_CHANNEL')
    def handle_channel_unarchived(data):
        print("\n[UNARCHIVED_CHANNEL] Канал разархирован:")
        print(f"Channel NAME: {data.get('name')}")
        print(f"Channel ID: {data.get('channelId')}")

    @sio.on('ARCHIVED_CHANNEL')
    def handle_channel_archived(data):
        print("\n[ARCHIVED_CHANNEL] Канал архирован:")
        print(f"Channel NAME: {data.get('name')}")
        print(f"Channel ID: {data.get('channelId')}")
    def connect_websocket_first_user(self):
        """Подключение к WebSocket"""
        try:
            sio.connect(
                'wss://api.dev.sphera.work/socket.io/',
                transports=['websocket'],
                auth={
                    'auth_token': self.auth_token_first_user,
                    'token': self.refresh_token_first_user,
                    'deviceId': DEVICE_ID_FIRST_USER,
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
