import socketio
from utils.logger import Logger
from API.api_auth import Authorization

sio = socketio.Client()
logger = Logger()


BASE_URL = "https://api.dev.sphera.work/api/v1"
CHECK_AND_SEND = BASE_URL + "/auth/email/check-and-send"
SIGN_IN = BASE_URL + "/auth/sign-in"
DEVICE_ID_FIRST_USER = "a8100b26-82e7-427e-b731-9ccbabcf62f5"
DEVICE_ID_SECOND_USER = "f6b7dbc5-7cc6-4905-928a-e9a57fa2abcb"
class WebSocket(Authorization):
    def __init__(self):
        super().__init__()
        api = Authorization()
        self.refresh_token_first_user = api.get_refresh_token_first_user()
        self.auth_token_first_user = api.get_auth_token_first_user()

        self.refresh_token_second_user = api.get_refresh_token_second_user()
        self.auth_token_second_user = api.get_auth_token_second_user()

        
    @sio.on('*')   
    def handle_any_event(event, data):
        """Обрабатывает ВСЕ события"""
        logger.info(f"[Все события] Получено {event}: {data}")

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

    def connect_websocket_second_user(self):
        """Подключение к WebSocket"""
        try:
            sio.connect(
                'wss://api.dev.sphera.work/socket.io/',
                transports=['websocket'],
                auth={
                    'auth_token': self.auth_token_second_user,
                    'token': self.refresh_token_second_user,
                    'deviceId': DEVICE_ID_SECOND_USER,
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
  