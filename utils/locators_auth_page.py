from selenium.webdriver.common.by import By

class AuthorizationLocators():
    EMAIL_FIELD = (By.CSS_SELECTOR, "[name='email']")

    EMAIL_ERROR_MESSAGE = (By.CLASS_NAME, "sphr-input__helper-text--bottom")
    
    SUBMIT_BUTTON = (By.CLASS_NAME, "submit-action-button")

    ONE_TIME_CODE = (By. ID, "one-time-code")

    ENTER_WORKSPACE_BUTTON = (By. CLASS_NAME, "sphr-button__title")

