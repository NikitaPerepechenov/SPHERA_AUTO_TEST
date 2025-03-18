from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        
    def refresh_page(self):
        self.browser.refresh() 


    def wait_element(self, locator):
        """Ожидание появления элемента на странице."""
        try:
            return WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Элемент {locator} не найден")

    def wait_elements(self, locator):
        """Ожидание появления элементов на странице."""
        try:
            return WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            print(f"Элемент {locator} не найден")

    def element_to_be_clickable(self, locator):
        """Ожидание, пока элемент станет кликабельным."""
        try:
            return WebDriverWait(self.browser, 20).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            print(f"Элемент {locator} не найден")



    def visibility_of_element(self, locator):
        """Ожидание пока элемент будет видимым"""
        try:
            return WebDriverWait(self.browser, 20).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Элемент {locator} не найден")  

    def visibility_of_elements(self, locator):
        """Ожидание пока элемент будет видимым"""
        try:
            return WebDriverWait(self.browser, 10).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            print(f"Элемент {locator} не найден")  



    def invis_of_element(self, locator):
        """Ожидание пока элемент будет neвидимым"""
        try:
            return WebDriverWait(self.browser, 10).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Элемент {locator} не найден")  


    def invisibility_of_all_elements(self, locator):
        """Ожидание, пока все элементы, найденные по локатору, станут невидимыми."""
        try:
            return WebDriverWait(self.browser, 10).until(
                lambda driver: all(not element.is_displayed() for element in driver.find_elements(*locator))
            )
        except TimeoutException:
            pass