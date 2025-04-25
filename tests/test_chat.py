import pytest
from faker import Faker
from pages.main_page import MainPage
from utils.websocket_client import WebSocket
from pages.login_page import AuthorizationPage
from API.payloads import AuthorizationPayloadReceiver 

auth = AuthorizationPayloadReceiver

fake = Faker('ru_RU')
random_message_text = fake.sentence()

email = "qa1@fusion.ru"
email2 = "qa2@fusion.ru"
code = "654321"
user = "Recieve"

@pytest.mark.chatik
def test_01_message_delivery(browser_1, browser_2):
    web = WebSocket()
    
    sender = MainPage(browser_1)  # Отправитель
    receiver = MainPage(browser_2)  # Получатель
    auth_page = AuthorizationPage(browser_1)
    receiver_auth = AuthorizationPage(browser_2)

    # Подключение к WebSocket
    auth = AuthorizationPayloadReceiver()
    web.connect_websocket_with_user(auth)

    # Авторизация отправителя
    auth_page.email_field(email)
    auth_page.submit_button()
    auth_page.one_time_code(code)
    auth_page.enter_workspace()
    auth_page.enter_space_button()

    # Отправка сообщения
    sender.create_message()
    sender.user_search_and_selection(user)
    sender.write_a_message(random_message_text)
    sender.send_message_user(random_message_text)
    sender.check_last_send_message(random_message_text)
    sender.browser_quit()

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

