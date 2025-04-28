import os
import json
import uuid
import shutil
import pytest
import tempfile
from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

dotenv_values(".env.dev")
config = dotenv_values(".env.dev")

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
    driver = webdriver.Chrome(options=options)

    driver.get(config.get("URL_SPHERA"))
    driver.maximize_window()
    yield driver

    driver.quit()
    shutil.rmtree(user_data_dir)

@pytest.fixture(scope="function")
def browser_1():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--remote-debugging-port=34222")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    user_data_dir = tempfile.mkdtemp(prefix=f"chrome_{uuid.uuid1()}_")
    options.add_argument(f"--user-data-dir={user_data_dir}")

    service = Service(executable_path="/snap/bin/chromedriver") # указать свой путь к драйверу
    driver = webdriver.Chrome(options=options)

    driver.get(config.get("URL_SPHERA"))
    driver.maximize_window()
    yield driver

    driver.quit()
    shutil.rmtree(user_data_dir)



@pytest.fixture(scope="function")
def browser_2():
    
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--remote-debugging-port=34223")
    options.add_argument("--headless")  

    user_data_dir = tempfile.mkdtemp(prefix=f"chrome_receiver_{uuid.uuid4()}_")
    options.add_argument(f"--user-data-dir={user_data_dir}")

    service = Service(executable_path="/snap/bin/chromedriver") # указать свой путь к драйверу
    driver = webdriver.Chrome(options=options)
    
    driver.get(config.get("URL_SPHERA"))
    driver.maximize_window()
    yield driver
    
    driver.quit()
    shutil.rmtree(user_data_dir)

