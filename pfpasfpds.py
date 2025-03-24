from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import json
import random
import string
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



def generate_random_string(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

rand_message = generate_random_string(5)
last_name = generate_random_string(10)
first_name = generate_random_string(10)
surname = generate_random_string(10)
info = generate_random_string(10)
rand_reply = generate_random_string(5)

action = ActionChains

email = "qa1@fusion.ru"
code = "654321"

browser = webdriver.Chrome()

    
browser.get("https://app.dev.sphera.work/")
browser.maximize_window()
with open("cookies.json", "r") as file:
    cookies = json.load(file)
for cookie in cookies:
    browser.add_cookie(cookie)
browser.refresh()


wait = WebDriverWait(browser, 10)


create_channel = wait.until(
    EC.visibility_of_all_elements_located((By. CLASS_NAME, "sphr-button__icon"))
)[1].click()







write_message = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "ql-editor"))
).send_keys("https://xn--80abh7bk0c.xn--p1ai/quote/432352")



send_message = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//button[text()="Отправить"]'))
).click()


































time.sleep(2)