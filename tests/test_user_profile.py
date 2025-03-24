from pages.user_profile_page import UserProfile
import random
import string
import pytest

def generate_random_string(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))


def test_05_open_user_profile_and_redact_info(browser): # Передаем фикстуру browser
    
    user = UserProfile(browser) # Создаем экземпляр UserProfile, передавая browser
    
    last_name = generate_random_string(10)# Генерация рандомной Фамилии пользователя
    first_name = generate_random_string(10)# Генерация рандомного Имени пользователя
    surname = generate_random_string(10) # Генерация рандомного Отчества пользователя
    info = generate_random_string(10) # Генерация рандомной информации в поле О себе
    
    user.open_user_profile_modal_window() # Клик по аватарке пользователя в футере приложения
    user.open_user_settings_in_modal_window() # В появившемся модальном окне клик по 'Настройки пользователя'
    
    user.edit_information_button() # В открывшейся странице профиля пользователя нажатие по кнопке редактирования личной информации
    user.user_last_name_field(last_name) # Очистка и ввод рандомной Фамилии
    user.user_first_name_field(first_name) # Очистка и ввод рандомного Имени
    user.user_surname_field(surname) # Очистка и ввод рандомного Отчества
    user.gender_male_radio_button() # Нажатие по радио-кнопке выбора Мужского пола
    user.user_info_field(info) # Заполнение поля О себе
    user.user_date_of_birth() # Выбор месяца Февраль и рандомного дня в плагине календаря
    
    user.save_button() # Сохранение заполненой информации
    
    user.check_last_name(last_name) # Проверка валидации поля Фамилия
    user.check_first_name(first_name) # Проверка валидации поля Имя
    user.check_surname(surname) # Проверка валидации поля Отчество
    user.check_radio_button_gender_male() # Проверка валидации радио-кнопки
    user.check_info(info) # Проверка валидации поля О себе
    