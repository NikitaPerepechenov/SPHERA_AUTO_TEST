from utils.logger import Logger
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from utils.main_page_locators import LocatorsMainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = Logger()

class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        self.locators = LocatorsMainPage
        
    def refresh_page(self):
        self.browser.refresh() 

    def scroll_chat_to_up(self):
        scroll = self.wait_element(
            self.locators.SCROLL_CHAT
        )
        self.browser.execute_script(
            "arguments[0].scrollTo({ top: 0, behavior: 'smooth' });", scroll
        )


    def scroll_chat_to_bottom(self):
        scroll = self.wait_element(
            self.locators.SCROLL_CHAT
        )
        self.browser.execute_script(
            "arguments[0].scrollTo({ top: arguments[0].scrollHeight, behavior: 'smooth' });", scroll
        )

    def wait_element(self, locator):
        """Ожидание появления элемента на странице."""
        try:
            return WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"Элемент {locator} не найден")

    def wait_elements(self, locator):
        """Ожидание появления элементов на странице."""
        try:
            return WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            logger.error(f"Элемент {locator} не найден")

    def wait_for_selector_inside_element(self, element, locator):
        """Ожидание появления элементов на странице."""
        try:
            return WebDriverWait(element, 10).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"Элемент {element} {locator} не найден")

    def element_to_be_clickable(self, locator):
        """Ожидание, пока элемент станет кликабельным."""
        try:
            return WebDriverWait(self.browser, 20).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            logger.error(f"Элемент {locator} не найден")



    def visibility_of_element(self, locator):
        """Ожидание пока элемент будет видимым"""
        try:
            return WebDriverWait(self.browser, 20).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"Элемент {locator} не найден")  

    def visibility_of_elements(self, locator):
        """Ожидание пока элемент будет видимым"""
        try:
            return WebDriverWait(self.browser, 10).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            logger.error(f"Элемент {locator} не найден")  
            



    def invis_of_element(self, locator):
        """Ожидание пока элемент будет neвидимым"""
        try:
            return WebDriverWait(self.browser, 10).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"Элемент {locator} не найден")  


    def invisibility_of_all_elements(self, locator):
        """Ожидание, пока все элементы, найденные по локатору, станут невидимыми."""
        try:
            return WebDriverWait(self.browser, 10).until(
                lambda driver: all(not element.is_displayed() for element in driver.find_elements(*locator))
            )
        except TimeoutException:
            pass