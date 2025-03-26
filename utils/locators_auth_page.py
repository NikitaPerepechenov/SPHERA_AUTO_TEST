from selenium.webdriver.common.by import By   

class AuthorizationLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, "[name='email']")
    
    SUBMIT_BUTTON = (By.CLASS_NAME, "submit-action-button")

    ONE_TIME_CODE = (By. ID, "one-time-code")

    ENTER_WORKSPACE_BUTTON = (By. CSS_SELECTOR, "button.sc-iXGltN.hysUdk")