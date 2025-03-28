import pytest
import random
import string
from pages.main_page import MainPage



def generate_random_string(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

random_message_text = generate_random_string(5)

user = "Senders"

@pytest.mark.chatik
def test_01_message_delivery(browser_1, browser_2):
    sender = MainPage(browser_1)  # Отправитель
    receiver = MainPage(browser_2)  # Получатель


    sender.create_message()  # Нажатие по плюсику
    sender.user_search_and_selection(user)  # Выбор пользователя
    sender.write_a_message(random_message_text) 
    sender.send_message_user(random_message_text)
    sender.check_last_send_message(random_message_text)  # Проверка у отправителя

    receiver.select_first_user()  # Выбор первого пользователя в сайд-баре
    receiver.check_last_send_message(random_message_text)  # Проверка у получателя
    
    