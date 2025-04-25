from utils.logger import Logger
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from utils.locators_auth_page import AuthorizationLocators
from selenium.webdriver.common.action_chains import ActionChains
import time

logger = Logger()


class AuthorizationPage(BasePage):
    def __init__(self, browser):
        self.browser = browser
        self.loc = AuthorizationLocators
        super(AuthorizationPage, self).__init__(browser)

    def email_field(self, email):
        """Ввод email"""
        try:
            logger.info(f"Ввод email: {email}")
            self.element_to_be_clickable(
                self.loc.EMAIL_FIELD
            ).send_keys(email)
            logger.info(f"Email: {email} введен")
        except Exception as e:
            logger.error(f"Не удалось ввести email: {email},  {e}")
            raise Exception(f"Не удалось ввести email: {email},  {e}")

    def submit_button(self):
        """Клик по кнопке 'Войти'"""
        try:
            logger.info("Клик по кнопке 'Войти'")
            self.element_to_be_clickable(
                self.loc.SUBMIT_BUTTON
            ).click()
            logger.info("Кнопка 'Войти' нажата")
        except Exception as e:
            raise logger.error(f"Не удалось нажать кнопку 'Войти': {e}")

    def one_time_code(self, code):
        """Ввод одноразового кода"""
        try:
            logger.info(f"Ввод одноразового кода: {code}")
            self.wait_element(
                self.loc.ONE_TIME_CODE
            ).send_keys(code)
            logger.info(f"Код: {code} введен")
        except Exception as e:
            raise logger.error(f"Не удалось ввести код: {code},  {e}")

    def enter_space_button(self):
        """Клик по кнопке 'Войти'"""
        try:
            logger.info("Клик по кнопке 'Войти'")
            a = self.visibility_of_elements(
                self.loc.ENTER_WORKSPACE_BUTTON)[1]
            self.element_to_be_clickable(a).click()
            logger.info("Кнопка 'Войти' нажата")
        except Exception as e:
            logger.error(f"Не удалось нажать кнопку 'Войти': {e}")
            raise Exception (f"Не удалось нажать кнопку 'Войти': {e}")
        

    def enter_workspace(self):
        """ Выбор рабочего пространства """
        try:
            logger.info("Выбор рабочего пространства 2 ")
            self.wait_elements(
                self.loc.CHOICE_SECOND_WORKSPACE)[0].click()
            self.wait_elements(
                self.loc.CHOICE_SECOND_WORKSPACE)[1].click()
            logger.info("Рабочее пространство 2 выбрано")
        except Exception as e:
            logger.error(f"Не удалось выбрать рабочее пространство: {e}")
    

    def test_invalid_emails(self, invalid_emails):
        action = ActionChains(self.browser)

        for index, invalid_email in enumerate(invalid_emails, 6):
            
            email_field = self.visibility_of_element(
                self.loc.EMAIL_FIELD
            )

            email_field.click()
            
            action.click(email_field)
            action.double_click(email_field).perform()
            email_field.send_keys(Keys.BACKSPACE)
                
            email_field.send_keys(invalid_email)
            email_field.send_keys(Keys.ENTER)
        
            try:
                error_message = self.visibility_of_element(
                    self.loc.EMAIL_ERROR_MESSAGE
                )
                logger.info(f"Тест {index}: Для '{invalid_email}' получена ошибка: {error_message.text}")
            except:
                logger.error(f"Тест {index}: Для '{invalid_email}' ошибка не обнаружена!")