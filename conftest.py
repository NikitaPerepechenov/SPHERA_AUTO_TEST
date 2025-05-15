import os
import uuid
import shutil
import pytest
import tempfile
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv(".env.dev", override=True)

def create_driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")

    user_data_dir = tempfile.mkdtemp(prefix=f"chrome_{uuid.uuid4()}_")
    options.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    return driver, user_data_dir

@pytest.fixture(scope="session")
def browser():
    driver, user_data_dir = create_driver()
    driver.get(os.getenv("URL_SPHERA"))
    driver.maximize_window()
    yield driver
    driver.quit()
    shutil.rmtree(user_data_dir)


@pytest.fixture(scope="function")
def browser_1():
    print("📌 browser_1: URL_SPHERA =", os.getenv("URL_SPHERA"))
    driver, user_data_dir = create_driver()
    driver.get(os.getenv("URL_SPHERA"))
    driver.maximize_window()
    yield driver
    driver.quit()
    shutil.rmtree(user_data_dir)


@pytest.fixture(scope="function")
def browser_2():
    driver, user_data_dir = create_driver()
    driver.get(os.getenv("URL_SPHERA"))
    driver.maximize_window()
    yield driver
    driver.quit()
    shutil.rmtree(user_data_dir)