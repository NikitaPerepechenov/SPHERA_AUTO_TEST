from utils.locators_auth_page import AuthorizationLocators
from utils.main_page_locators import LocatorsMainPage
from utils.logger import Logger
from pages.base_page import BasePage

logger = Logger()

class AuthorizationPage(BasePage):
    def __init__(self, browser):
        self.browser = browser
        self.locators = AuthorizationLocators
        self.main = LocatorsMainPage
        super(AuthorizationPage, self).__init__(browser)

    def email_field(self, email):
        """Ввод email"""
        try:
            logger.info(f"Ввод email: {email}")
            self.visibility_of_element(
                self.locators.EMAIL_FIELD
            ).send_keys(email)
            logger.info(f"Email: {email} введен")
        except Exception as e:
            raise logger.error(f"Не удалось ввести email: {email},  {e}")

    def submit_button(self):
        """Клик по кнопке 'Войти'"""
        try:
            logger.info("Клик по кнопке 'Войти'")
            self.element_to_be_clickable(
                self.locators.SUBMIT_BUTTON
            ).click()
            logger.info("Кнопка 'Войти' нажата")
        except Exception as e:
            raise logger.error(f"Не удалось нажать кнопку 'Войти': {e}")

    def one_time_code(self, code):
        """Ввод одноразового кода"""
        try:
            logger.info(f"Ввод одноразового кода: {code}")
            self.wait_element(
                self.locators.ONE_TIME_CODE
            ).send_keys(code)
            logger.info(f"Код: {code} введен")
        except Exception as e:
            raise logger.error(f"Не удалось ввести код: {code},  {e}")

    def enter_space_button(self):
        """Клик по кнопке 'Войти'"""
        try:
            logger.info("Клик по кнопке 'Войти'")
            self.element_to_be_clickable(
                self.locators.ENTER_WORKSPACE_BUTTON
            ).click()
            logger.info("Кнопка 'Войти' нажата")
        except Exception as e:
            raise logger.error(f"Не удалось нажать кнопку 'Войти': {e}")
    
