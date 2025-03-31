from selenium.webdriver.common.by import By

from utils.main_page_locators import LocatorsMainPage

class AuthorizationLocators(LocatorsMainPage):
    EMAIL_FIELD = (By.CSS_SELECTOR, "[name='email']")
    
    SUBMIT_BUTTON = (By.CLASS_NAME, "submit-action-button")

    ONE_TIME_CODE = (By. ID, "one-time-code")

    ENTER_WORKSPACE_BUTTON = (By. CLASS_NAME, "sphr-button__title")