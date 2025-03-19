import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tempfile
import shutil
import uuid

@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=34221")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    

    user_data_dir = tempfile.mkdtemp(prefix=f"chrome_{uuid.uuid1()}_")
    options.add_argument(f"--user-data-dir={user_data_dir}")

    service = Service(executable_path="/snap/bin/chromedriver") # указать свой путь к драйверу
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://app.staging.sphera.work/")
    driver.maximize_window()

    # Выполните авторизацию здесь, если это необходимо
    yield driver

    driver.quit()
    shutil.rmtree(user_data_dir)