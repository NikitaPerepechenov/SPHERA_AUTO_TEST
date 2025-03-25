from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.logger import Logger

logger = Logger()

class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        
    def refresh_page(self):
        self.browser.refresh() 


    def scroll_chat_to_bottom(self, attempts=3):
        """Надежная прокрутка чата вниз"""
        for attempt in range(attempts):
            try:
                chat_container = self.wait_element(
                    (By.CLASS_NAME, "__messages-observe-container__")
                    
                )
               
                self.browser.execute_script(
                    "arguments[0].scrollTop = arguments[0].scrollHeight;", 
                    chat_container
                )
              
                current_pos = self.browser.execute_script(
                    "return arguments[0].scrollTop;", 
                    chat_container
                )
                max_height = self.browser.execute_script(
                    "return arguments[0].scrollHeight;", 
                    chat_container
                )
                if max_height - current_pos < 100: 
                    return True
                
            except Exception as e:
                logger.error(f"Попытка {attempt + 1}: Ошибка прокрутки - {str(e)}")
                raise Exception("Не удалось прокрутить чат до конца")
            
    def scroll_to_element(self, element, attempts=3):
        """Прокручивает контейнер чата до указанного элемента"""
        for attempt in range(attempts):
            try:
                # 1. Находим контейнер чата
                chat_container = self.wait_element(
                    (By.CLASS_NAME, "__messages-observe-container__")
                    
                )
                
                # 2. Получаем позицию элемента относительно контейнера
                element_pos = self.browser.execute_script(
                    "return arguments[1].offsetTop - arguments[0].offsetTop;",
                    chat_container,
                    element
                )
                
                # 3. Вычисляем видимую область контейнера
                container_height = self.browser.execute_script(
                    "return arguments[0].clientHeight;",
                    chat_container
                )
                
                # 4. Прокручиваем к элементу (с центрированием)
                self.browser.execute_script(
                    """
                    arguments[0].scrollTop = arguments[1] - (arguments[2] / 2) + (arguments[3] / 2);
                    """,
                    chat_container,
                    element_pos,
                    element.size['height'],
                    container_height
                )
                
                # 5. Проверяем видимость элемента
                if self.is_element_visible_in_container(element, chat_container):
                    return True
                    
           
            
            except Exception as e:
                logger.error(f"Попытка {attempt + 1}: Ошибка прокрутки - {str(e)}")
                if attempt == attempts - 1:
                    raise Exception(f"Не удалось прокрутить к элементу после {attempts} попыток")



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