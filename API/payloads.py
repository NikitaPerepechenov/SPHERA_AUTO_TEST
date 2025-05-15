import os
from faker import Faker
from dotenv import load_dotenv

load_dotenv(".env.dev", override=True)

fake = Faker('ru_RU')

name = fake.word()
description = fake.word()

class AuthorizationPayloadSender:
    device_id = os.getenv("DEVICE_ID_FIRST")
    check_and_send_payload = {
        "email": "qa1@fusion.ru"
    }

    sign_in = {
        "code": "654321",
        "email": "qa1@fusion.ru"
    }

class AuthorizationPayloadReceiver:
    device_id = os.getenv("DEVICE_ID_SECOND")
    check_and_send_payload = {
        "email": "qa2@fusion.ru"
    }

    sign_in = {
        "code": "654321",
        "email": "qa2@fusion.ru"
    }



class ChannelsPayload:
    channel_create_payload = {
        "name": name,
        "isPrivate": False,
        "description": description,
        "icon": ":orangutan:",
        "limitedAccess": False
    }
 
    get_channel_by_name = {
      "name": name,
      "companyId": 82
    }

