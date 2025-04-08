import os
import random
import string

def generate_random_string(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

name = generate_random_string(5)
description = generate_random_string(5)

class AuthorizationPayload:
    device_id = os.getenv("DEVICE_ID_FIRST")
    check_and_send_payload = {
        "email": "qa1@fusion.ru"
    }

    sign_in = {
        "code": "654321",
        "email": "qa1@fusion.ru"
    }

class AuthorizationPayload2:
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

