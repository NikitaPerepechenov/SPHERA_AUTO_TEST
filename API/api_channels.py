import requests
from utils.logger import Logger
from api_auth import Authorization
from payloads import ChannelsPayload as channels
# URL
BASE_URL = "https://api.dev.sphera.work/api/v1/"
CHANNELS_CREATE_URL = BASE_URL + "channels/create"
GET_CHANNELS = BASE_URL + "channels/users-channels"
DELETE_CHANNEL_BY_ID = BASE_URL + "channels/delete/" # ID
ARCHIVE_CHANNEL_BY_ID = BASE_URL + "channels/""/toggle-archive-status"

#HEADERS
AUTHORIZATION_HEADER = "authorization"
CONTENT_TYPE_HEADER = "content-type"
HEADER_DEVICE_ID_FIRST_USER = "device-id"
HEADER_DEVICE_ID_SECOND_USER = "device-id"

logger = Logger()

class Channels:
    def __init__(self):
        self.auth = Authorization()

        self.refresh_token = self.auth.get_refresh_token_first_user()
        
        self.default_headers = {
            CONTENT_TYPE_HEADER: "application/json",
            HEADER_DEVICE_ID_FIRST_USER: "a8100b26-82e7-427e-b731-9ccbabcf62f5"
        }

    def create_channel(self):

        headers = {
            **self.default_headers,
            AUTHORIZATION_HEADER: f"Bearer {self.refresh_token}"
        }
        
        payload = channels.channel_create_payload

        try:
            response = requests.post(
                CHANNELS_CREATE_URL, 
                headers=headers, 
                json=payload
            )
            response.raise_for_status()
            
            channel_data = response.json()
            self.channel_name = channel_data.get("name", payload.get("name"))
            

            if self.channel_name:
                logger.info(f"Канал создан: {self.channel_name}")
            else:
                logger.error("Канал создан, но название отсутствует в ответе")
            
            return channel_data

        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при создании канала: {e}")
        except requests.exceptions.InvalidJSONError as e:
            logger.error(f"Не верный формат JSON: {e}")
        except requests.exceptions.InvalidHeader as e:
            logger.error(f"Не верный headers: {e}")
        

                
    def check_channel_by_name(self):
        headers = {
            **self.default_headers,
            AUTHORIZATION_HEADER: f"Bearer {self.refresh_token}"
        }
        
        try: 
            response = requests.get(
                GET_CHANNELS, 
                headers=headers, 
            )
            response.raise_for_status()
            channel_data = response.json()
            
            found_channel = None
            for channel in channel_data.get("payload").get("channels"): 
                if channel["name"] == self.channel_name:
                    found_channel = channel
                    break
            
            if found_channel:
                self.channel_id = found_channel['channelId']
                logger.info(f"Найден канал: {found_channel['name']} (ID: {found_channel['channelId']})")
            else:
                self.channel_id = None
                logger.error(f"Канал '{self.channel_name}' не найден")
                
            return found_channel
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при проверке канала: {e}")
        except requests.exceptions.InvalidJSONError as e:
            logger.error(f"Не верный формат JSON: {e}")
        except requests.exceptions.ReadTimeout as e:
            logger.error(f"Таймаут при отправке данных канала: {e}")

    def archive_channel_by_id(self):
        url = f"{BASE_URL}channels/{self.channel_id}/toggle-archive-status"
        headers = {
            **self.default_headers,
            AUTHORIZATION_HEADER: f"Bearer {self.refresh_token}"
        }

        try: 
            response = requests.patch(url, headers=headers)
            response.raise_for_status()
            channel_data = response.json()

            channel_name = channel_data.get("payload", {}).get("name")
            is_archived = channel_data.get("payload", {}).get("isArchived", True)
            
            if is_archived:
                logger.info(f"Канал '{channel_name}' (ID: {self.channel_id}) успешно архивирован")
            else:
                logger.error(f"Не удалось архивировать канал '{channel_name}' (ID: {self.channel_id})")
                
            return channel_data
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при архивации канала ID {self.channel_id}: {e}")
        except requests.exceptions.InvalidJSONError as e:
            logger.error(f"Не верный формат JSON: {e}")


    def delete_channel_by_id(self):
        headers = {
            **self.default_headers,
            AUTHORIZATION_HEADER: f"Bearer {self.refresh_token}"
        }

        try: 
            response = requests.delete(
                f"{DELETE_CHANNEL_BY_ID}{self.channel_id}", 
                headers=headers, 
            )
            assert response.status_code == 204, "Канал не удален"
            logger.info(f"Канал {self.channel_id} удален")
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при удалении канала:({self.channel_id}), {e}")
        except requests.exceptions.InvalidJSONError as e:
            logger.error(f"Не верный формат JSON: {e}")
            
        
