import pytest
from faker import Faker
from pages.user_profile_page import UserProfile

fake = Faker('ru_RU')



@pytest.mark.u
def test_07_open_user_profile_and_redact_info(browser): # Передаем фикстуру browser
    
    user = UserProfile(browser) # Создаем экземпляр UserProfile, передавая browser
    
    last_name = fake.last_name()# Генерация рандомной Фамилии пользователя
    first_name = fake.first_name()# Генерация рандомного Имени пользователя
    surname = fake.middle_name_male() # Генерация рандомного Отчества пользователя
    info = fake.text() # Генерация рандомной информации в поле О себе
    
    user.open_user_profile_modal_window().open_user_settings_in_modal_window()
    
    user.edit_information_button().user_last_name_field(last_name).user_first_name_field(first_name).user_surname_field(surname)
    user.gender_male_radio_button().user_info_field(info).user_date_of_birth().save_button()
    
    user.check_last_name(last_name).check_first_name(first_name).check_surname(surname).check_radio_button_gender_male().check_info(info)
    # Проверка валидации полей профиля

    