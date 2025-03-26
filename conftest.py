import json
import uuid
import shutil
import pytest
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--remote-debugging-port=34221")
    # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")
    

    user_data_dir = tempfile.mkdtemp(prefix=f"chrome_{uuid.uuid1()}_")
    options.add_argument(f"--user-data-dir={user_data_dir}")

    # service = Service(executable_path="/snap/bin/chromedriver") # указать свой путь к драйверу
    driver = webdriver.Chrome(options=options)

    driver.get("https://app.dev.sphera.work/")
    driver.maximize_window()
    with open("cookies.json", "r") as file:
        cookies = json.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    yield driver

    driver.quit()
    shutil.rmtree(user_data_dir)

@pytest.fixture(scope="function")
def browser_1():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=34222")
    # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")
    

    user_data_dir = tempfile.mkdtemp(prefix=f"chrome_{uuid.uuid1()}_")
    options.add_argument(f"--user-data-dir={user_data_dir}")

    # service = Service(executable_path="/snap/bin/chromedriver") # указать свой путь к драйверу
    driver = webdriver.Chrome(options=options)

    driver.get("https://app.dev.sphera.work/")
    driver.maximize_window()
    with open("cookies.json", "r") as file:
        cookies = json.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    yield driver

    driver.quit()
    shutil.rmtree(user_data_dir)



@pytest.fixture(scope="function")
def browser_2():
    
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=34223")
    # options.add_argument("--headless")  

    user_data_dir = tempfile.mkdtemp(prefix=f"chrome_receiver_{uuid.uuid4()}_")
    options.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(options=options)
    driver.get("https://app.dev.sphera.work/")
    
    
    with open("cookies2.json", "r") as file:
        cookies = json.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    
    yield driver
    
    driver.quit()
    shutil.rmtree(user_data_dir)





