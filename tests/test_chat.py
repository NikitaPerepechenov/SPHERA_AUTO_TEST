import pytest
import random
import string
from pages.main_page import MainPage
from tests.websocket_client import WebSocket
from pages.login_page import AuthorizationPage


def generate_random_string(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

random_message_text = generate_random_string(5)

email = "qa1@fusion.ru"
email2 = "qa2@fusion.ru"
code = "654321"
user = "Senders"

@pytest.mark.chatik
def test_04message_delivery(browser_1, browser_2):
    sender = MainPage(browser_1)  # Отправитель
    web = WebSocket()
    receiver = MainPage(browser_2)  # Получатель
    auth_page = AuthorizationPage(browser_1)
    receiver_auth = AuthorizationPage(browser_2)

    # Подключение к WebSocket
    web.connect_websocket_first_user()

    # Авторизация отправителя
    auth_page.email_field(email)
    auth_page.submit_button()
    auth_page.one_time_code(code)
    auth_page.enter_space_button()

    # Отправка сообщения
    sender.create_message()
    sender.user_search_and_selection(user)
    sender.write_a_message(random_message_text)
    sender.send_message_user(random_message_text)
    sender.check_last_send_message(random_message_text)

    # Авторизация получателя
    receiver_auth.email_field(email2)
    receiver_auth.submit_button()
    receiver_auth.one_time_code(code)
    receiver_auth.enter_space_button()

    # Проверка получения сообщения
    receiver.select_first_user()
    receiver.check_last_send_message(random_message_text)

    #Отключение WebSocket
    web.disconnect_websocket()

