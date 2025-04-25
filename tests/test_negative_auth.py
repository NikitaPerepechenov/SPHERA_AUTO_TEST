import pytest
from faker import Faker
from utils.logger import Logger
from pages.login_page import AuthorizationPage

fake = Faker()
logger = Logger()


invalid_emails = [
    f"@{fake.domain_name()}",              # Отсутствует локальная часть
    f"{fake.user_name()}@",                # Нет домена
    f"{fake.user_name()}@{fake.word()}",   # Домен без точки
    f"{'a'*256}@example.com",              # Слишком длинный email
    "me@.com",                             # Домен начинается с точки
    "john.doe@-example.com",               # Домен начинается с дефиса
    "тест@example.com",                    # Кириллица в локальной части
    "user@example..com",                   # Две точки подряд в домене
    "user@example_com",                    # Подчеркивание в домене
    "user@.com"                            # Пустой домен
]

@pytest.mark.qwe
def test_06_negative_auth(browser):
    auth_page = AuthorizationPage(browser)
    auth_page.test_invalid_emails(invalid_emails)