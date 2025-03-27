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
def test_01_message_delivery(browser_1):
    main = MainPage(browser_1) # Отправитель
  

    main.create_message() # Нажатие по плюсику написать сообщение
    main.user_search_and_selection(user) # Ввод и выбор пользователя
    main.write_a_message(random_message_text) 
    main.send_message_user()
    main.check_last_send_message(random_message_text) # Проверка отображения и отправки сообщения 

    # main = MainPage(browser_2)
    # main.select_first_user()
    # main.check_last_send_message(random_message_text)

@pytest.mark.chatik
def test_02_message_delivery_accept(browser_2):
    main = MainPage(browser_2) # Получатель

    main.select_first_user() # Выбор первого пользователя в сайд-баре слева
    main.check_last_send_message(random_message_text)
    
    