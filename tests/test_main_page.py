import pytest
import random
import string
from pages.main_page import MainPage
from pages.login_page import AuthorizationPage


def generate_random_string(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

email = "qa1@fusion.ru"
code = "654321"

@pytest.mark.skip
def test_02_authorization(browser):
    auth_page = AuthorizationPage(browser)
    auth_page.email_field(email) # Ввод email
    auth_page.submit_button() # Нажатие кнопки 'Получить код'
    auth_page.one_time_code(code) # Ввод одноразового кода
    auth_page.enter_space_button() # Вход в пространство 


def test_03_create_channel_write_message_delete_channel(browser):  # Передаем фикстуру browser    
    main = MainPage(browser)  # Создаем экземпляр MainPage, передавая browser

    name_channel = generate_random_string(5) 
    info_channel = generate_random_string(5) 
    random_message_text = generate_random_string(5)

    main.decline_notifications() 
    main.create_channel_button() # Нажатие кнопки 'Создать канал'
    main.enter_name_channel(name_channel) # Ввод названия канала
    main.channel_info(info_channel) # Ввод описания канала
    main.channel_creation_confirmation_button() # Нажатие кнопки 'продолжить' после заполнения всех обязательных полей после создания канала
    
    main.waiting_for_modal_window_to_close() # Ожидание закрытия модального окна
    
    main.write_a_message(random_message_text) # Ввод сообщения в созданный канал
    main.send_message() # Отправка сообщения в созданный канал
    main.check_message(random_message_text) # Проверка отправки сообщения
    
    main.header_button_channel() # Вызов модального окна через название канала в хедере приложения
    main.settings_tab_in_modal_window() # вкладка настройки в модальном окне
    main.delete_channel() # Удаление канала
    main.waiting_notifications_delete_close() # Ожидание закрытия уведомления об удалении канала
    # main.delete_channel_notifications_check() # Проверка уведомления об удалении канала
    main.check_channel_deleted(name_channel) # Проверка удаления канала из левого сайд бара


def test_04_create_channel_and_archive_channel(browser):
    
    main = MainPage(browser)

    name_channel = generate_random_string(5)
    info_channel = generate_random_string(5)
    
    main.create_channel_button() # Нажатие кнопки 'Создать канал'
    main.enter_name_channel(name_channel) # Ввод названия канала
    main.channel_info(info_channel) # Ввод описания канала
    main.channel_creation_confirmation_button() # Нажатие кнопки 'продолжить' после заполнения всех обязательных полей после создания канала
    
    main.waiting_for_modal_window_to_close() # Ожидание закрытия модального окна
    
    main.header_button_channel() # Вызов модального окна через название канала в хедере приложения
    main.settings_tab_in_modal_window() # вкладка настройки в модальном окне
    main.archive_channel() # Архивирование канала
    main.archive_channel_notifications_check() # Проверка уведомления об архивировании канала
    main.button_all_archive_channels() # Открытие вкладки Архив 
    main.archive_channel_check(name_channel) # Проверка заархивированного канала 
    main.back() 
 

def test_05_enter_random_channel_write_message_edit_reply_and_delete_message(browser):
    main = MainPage(browser)

    random_message_text = generate_random_string(5)
    edit_message = generate_random_string(5)
    rand_reply = generate_random_string(5)
    disc_message = generate_random_string(5)

    main.enter_in_random_channel() # Вход в рандомный канал
   
    main.write_a_message(random_message_text) # Ввод сообщения в поле ввода
    main.send_message() # Отправка сообщения кликом по кнопке 'Отправить'
    main.edit_last_message(edit_message) # Редактирования последнего сообщения в чате
    main.send_message() # Отправка отредактированного сообщения
    main.check_edit_message(edit_message) # Проверка отредактированного текста
    
    main.reply_message(rand_reply) # Ответ на сообщение 
    main.send_message()
    main.check_reply_message()

    main.other_actions() # Нажатие кнопки другие действия (сообщения)
    main.delete_message() # Удаление сообщения 
    main.message_deletion_check(random_message_text) # Проверка удаления сообщения 
    
    main.open_discussions_and_write_message(disc_message) # Открытие обсуждения
    main.write_a_wessage_with_link() # Отправка сообщения с линком 
