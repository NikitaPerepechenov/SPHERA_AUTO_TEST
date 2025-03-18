import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def browser():
    # Настройка опций Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Запуск в headless-режиме
    chrome_options.add_argument("--disable-gpu")  # Отключение GPU (для headless)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://app.staging.sphera.work/")
    driver.maximize_window()

    yield driver
    driver.quit()