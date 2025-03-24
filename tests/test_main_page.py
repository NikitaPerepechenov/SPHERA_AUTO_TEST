from pages.login_page import AuthorizationPage
from pages.main_page import MainPage
import random
import string
import pytest


def generate_random_string(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

email = "qa1@fusion.ru"
code = "654321"

@pytest.mark.skip
def test_01_authorization(browser):
    auth_page = AuthorizationPage(browser)
    auth_page.email_field(email) # Ввод email
    auth_page.submit_button() # Нажатие кнопки 'Получить код'
    auth_page.one_time_code(code) # Ввод одноразового кода
    auth_page.enter_space_button() # Вход в пространство
    # auth_page.decline_notifications()

@pytest.mark.skip
def test_02_create_channel_send_message__and_delete_channel(browser):  # Передаем фикстуру browser
    main = MainPage(browser)  # Создаем экземпляр MainPage, передавая browser
    name_channel = generate_random_string(5) 
    info_channel = generate_random_string(5) 
    rand_message = generate_random_string(5)

    main.create_channel_button() # Нажатие кнопки 'Создать канал'
    main.enter_name_channel(name_channel) # Ввод названия канала
    main.channel_info(info_channel) # Ввод описания канала
    main.channel_creation_confirmation_button() # Нажатие кнопки 'продолжить' после заполнения всех обязательных полей после создания канала
    
    main.Waiting_for_modal_window_to_close() # Ожидание закрытия модального окна
    main.write_a_message(rand_message) # Ввод сообщения в созданный канал
    main.send_message() # Отправка сообщения в созданный канал
    main.check_message(rand_message) # Проверка отправки сообщения
    
    main.header_button_channel() # Вызов модального окна через название канала в хедере приложения
    main.settings_tab_in_modal_window() # вкладка настройки в модальном окне
    main.archive_channel() # Архивирование канала
    main.archive_channel_notifications_check() # Проверка уведомления об архивировании канала



def test_03_create_channel__and_delete_channel(browser):
    log = AuthorizationPage(browser)
    
    main = MainPage(browser)
    name_channel = generate_random_string(5)
    info_channel = generate_random_string(5)
    
    main.create_channel_button() # Нажатие кнопки 'Создать канал'
    main.enter_name_channel(name_channel) # Ввод названия канала
    main.channel_info(info_channel) # Ввод описания канала
    main.channel_creation_confirmation_button() # Нажатие кнопки 'продолжить' после заполнения всех обязательных полей после создания канала
    
    main.Waiting_for_modal_window_to_close() # Ожидание закрытия модального окна
    
    main.header_button_channel() # Вызов модального окна через название канала в хедере приложения
    main.settings_tab_in_modal_window() # вкладка настройки в модальном окне
    main.delete_channel() # Удаление канала
    # log.decline_notifications()
    
    main.delete_channel_notifications_check() # Проверка уведомления об удалении канала
    main.delete_channel_check(name_channel) # Проверка удаления канала из левого сайд бара


def test_04_enter_random_channel_write_message_delete_message(browser):
    main = MainPage(browser)
    rand_message = generate_random_string(5)

    main.enter_in_random_channel() # Вход в рандомный канал
    main.write_a_message(rand_message) # Ввод сообщения в поле ввода
    main.send_message() # Отправка сообщения кликом по кнопке 'Отправить'
    main.delete_message() # Удаление сообщения 
    main.message_deletion_check(rand_message) # Проверка удаления сообщения 


