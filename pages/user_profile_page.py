import random
from utils.logger import Logger
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.main_page_locators import LocatorsMainPage
from selenium.webdriver.support.ui import WebDriverWait
from utils.user_profile_locators import LocatorsUserProfile
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException

logger = Logger()

class UserProfile(BasePage):
    def __init__(self, browser):
        """Инициализация класса.
        Объект браузера (WebDriver).
        """
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)
        self.locators = LocatorsUserProfile
        self.loc = LocatorsMainPage
        super(UserProfile, self).__init__(browser)


    def _check_field(self, locator, expected_text, field_name):
        """
        Универсальный метод для проверки текста в поле.
        
        :param locator: Локатор элемента.
        :param expected_text: Ожидаемый текст.
        :param field_name: Название поля для логирования.
        """
        try:
            logger.info(f"Проверка поля '{field_name}'")
            elements = self.wait_elements(locator)
            if not elements:
                raise NoSuchElementException(f"Элемент '{field_name}' не найден")
            
            actual_text = elements[0].text
            assert actual_text == expected_text, \
                f"Ошибка в поле '{field_name}': ожидалось '{expected_text}', получено '{actual_text}'"
            
            logger.info(f"Проверка поля '{field_name}' успешна")
        except (TimeoutException, NoSuchElementException, AssertionError) as e:
            raise logger.error(f"Ошибка при проверке поля '{field_name}': {str(e)}")
            

    def open_user_profile_modal_window(self):
        """ Нажатие по аватару пользователя в хедере приложения """
        
        try:
            logger.info("Нажатие по аватару пользователя в хедере приложения")
            self.visibility_of_elements(
            self.locators.PROFILE_MODAL
            )[1].click()
            logger.info("Успешное нажатие по аватару пользователя")
            logger.info('Ожидание появления модального окна')
            self.visibility_of_element(self.locators.PROFILE_MODAL_WAIT)
            logger.info(' Модальное окно успешно открыто')
        except Exception as e:
            raise logger.error(f"Не удалось нажать по аватару пользователя в хедере приложения {e}")
            


    def open_user_settings_in_modal_window(self):
        """ Нажатие кнопкни 
        'Настройки пользователя' в открывшемся модальном окне' """
        
        try:
            logger.info("Попытка нажатие кнопкни 'Настройки пользователя'")
            self.visibility_of_elements(
            self.locators.USER_PROFILE_SETTINGS
            )[0].click()
            logger.info("Успешное нажатие по кнопке 'Настройки пользователя' ")
        except Exception as e:
            raise logger.error(f"Не удалось нажать на кнопку 'Настройки пользователя' {e}")
            


    def edit_information_button(self):
        """ Нажатие кнопки редактирование информации """
        try:
            logger.info("Попытка нажатия кнопки редактирования информации")
            self.visibility_of_elements(
            self.locators.REDACT_USER_INFO
            )[2].click()
            logger.info("Успешное нажатие кнопки редактирования информации")
        except Exception as e:
            raise logger.error(f"Не удалось нажать кнопку редактирования информации {e}")
            

    def user_last_name_field(self, last_name):
        """ Редактирование поля 'Фамилия' """
        try:
            logger.info("Редактирование поля 'Фамилия'")
            action = ActionChains(self.browser)
            last_name_field = self.wait_element(self.locators.LAST_NAME_FIELD)
            

            logger.info("Поле 'Фамилия' не пустое. Очистка поля.")
            action.double_click(last_name_field).perform()
            last_name_field.send_keys(Keys.BACKSPACE)
            
            logger.info("Поле 'Фамилия' успешно очищено.")

            logger.info(f"Заполнение поля 'Имя' значением: {last_name}")
            last_name_field.send_keys(last_name)
            logger.info(f"Поле 'Фамилия' успешно заполнено значением: {last_name}")

        except Exception as e:
            raise logger.error(f"Не удалось заполнить поле 'Фамилия': {e}")
            


    def user_first_name_field(self, first_name):
        """Редактирование поля 'Имя'."""
        try:
            logger.info("Редактирование поля 'Имя'")

            first_name_field = self.wait_element(self.locators.FIRST_NAME_FIELD)
            action = ActionChains(self.browser)
            logger.info("Поле 'Имя' не пустое. Очистка поля.")
            action.double_click(first_name_field).perform()
            first_name_field.send_keys(Keys.BACKSPACE)      
            logger.info("Поле 'Имя' успешно очищено.")

            logger.info(f"Заполнение поля 'Имя' значением: {first_name}")
            first_name_field.send_keys(first_name)
            logger.info(f"Поле 'Имя' успешно заполнено значением: {first_name}")

        except Exception as e:
            raise logger.error(f"Не удалось заполнить поле 'Имя': {e}")
            

    def user_surname_field(self, surname):
        """ Редактирование поля 'Отчество' """
        try:
            logger.info("Редактирование поля 'Имя'")

            surname_field = self.wait_element(self.locators.SURNAME_FIELD)
            action = ActionChains(self.browser)
            logger.info("Поле 'Имя' не пустое. Очистка поля.")
            action.double_click(surname_field).perform() 
            surname_field.send_keys(Keys.BACKSPACE)     
            logger.info("Поле 'Имя' успешно очищено.")

            logger.info(f"Заполнение поля 'Имя' значением: {surname}")
            surname_field.send_keys(surname)
            logger.info(f"Поле 'Имя' успешно заполнено значением: {surname}")

        except Exception as e:
            raise logger.error(f"Не удалось заполнить поле 'Имя': {e}")
            

    def gender_male_radio_button(self):
        """ Клик по радио-кнопке 'Мужской'  """
        try:
            logger.info(" Клик по радио-кнопке выбора мужского пола ")
            self.wait_elements(
            self.locators.GENDER_MALE_RADIO_BUTTON
            )[0].click()
            
            logger.info(" Радио-кнопка выбора мужского пола нажата ")
        except Exception as e:
            raise logger.error(" Радио-кнопка выбора мужского пола не нажата ")
            


    def user_info_field(self, info):
        """ Редактирование поля 'О себе' """
        try:
            logger.info(" Попытка редактирования поля О себе ")
            self.wait_elements(
            self.locators.USER_INFO_FIELD
            )[4].click()

            info_field = self.wait_elements(
            self.locators.INPUT_INFO
            )[0]
            action = ActionChains(self.browser)
            info_field.click()
            action.double_click(info_field).perform()
            info_field.send_keys(Keys.BACKSPACE)

            self.wait_elements(
            self.locators.INPUT_INFO
            )[0].send_keys(info)

            
            logger.info(" Поле О себе успешно заполнено ")
        except Exception as e:
            raise logger.error(f"Не удалось отредактировать поле О себе {e}")
            

    
    def user_date_of_birth(self):
        """ Выбор рандомной даты рождения через плагин календаря """
        try:
            logger.info("Вызов плагина календаря")
            self.wait_element(
            self.locators.DATE_OF_BIRTH_REACT_PLUGIN
            ).click()
            logger.info("Выбор 'Февраль' ")
            february = self.visibility_of_elements(
            self.locators.FEBRUARY_MONTH
            )[1]
            february.click()
            logger.info("Месяц Февраль выбран")

            logger.info("Ожидание появления элемента")
            self.visibility_of_element(
            self.locators.DATE_OF_BIRTH_PLUGIN
            )

            week = self.visibility_of_elements(
            self.locators.WEEK_DATE_OF_BIRTH_PLUGIN
            )
            random.choice(week).click()
            logger.info("Рандомная дата рождения успешно выбрана через плагин календаря")
        except Exception as e:
            raise logger.error(f"Не удалось выбрать дату рождения через плагин календаря {e}")
            


    def save_button(self):
        """ Нажатие кнопки сохранить после заполнения всех полей """
        try:
            logger.info(" Нажатие кнопки Сохранить ")
            self.wait_elements(
            self.locators.SAVE_BUTTON
            )[1].click()
            logger.info("Кнопка Сохранить успешно нажата")
            
            logger.info("Ожидание скрытия кнопки Сохранить")
            self.invisibility_of_all_elements(self.locators.SAVE_BUTTON)
        except Exception as e:
            logger.error(f" Не удалось нажать кнопку Сохранить  {e}")
            raise

    def check_last_name(self, last_name):
        """Проверка успешного сохранения информации в поле 'Фамилия'."""
        try:
            logger.info("Проверка успешного сохранения информации в поле 'Фамилия'")
            self._check_field(self.locators.LAST_NAME_ASSERT, last_name, "Фамилия")
        except Exception as e:
            raise logger.error(f"Не удалось проверить поле 'Фамилия' {e}")
            

    def check_first_name(self, first_name):
        """Проверка успешного сохранения информации в поле 'Имя'."""
        try:
            logger.info("Проверка успешного сохранения информации в поле 'Имя'")
            self._check_field(self.locators.FIRST_NAME_ASSERT, first_name, "Имя")
        except Exception as e:
            raise logger.error(f"Не удалось проверить поле 'Имя' {e}")
            


    def check_surname(self, surname):
        """Проверка успешного сохранения информации в поле 'Отчество'."""
        try:
            logger.info("Проверка успешного сохранения информации в поле 'Отчество'")    
            self._check_field(self.locators.SURNAME_ASSERT, surname, "Отчество")
        except Exception as e:
            raise logger.error(f"Не удалось проверить поле 'Отчество' {e}")
            


    def check_info(self, info):
        """Проверка успешного сохранения информации в поле 'О себе'."""
        try:
            logger.info("Проверка успешного сохранения информации в поле 'О себе'")    
            self._check_field(self.locators.USER_INFO_ASSERT, info, "О себе")
        except Exception as e:
            raise logger.error(f"Не удалось проверить поле 'О себе' {e}")
            

    def check_radio_button_gender_male(self):
        """ Проверка успешного сохранении информации 
        радио-кнопки выбор пола 'Мужской' """
        try:
            logger.info("Проверка радио-кнопки мужского пола")
            check = self.wait_elements(
            self.locators.GENDER_MALE_RADIO_BUTTON_ASSERT
            )[0]
            assert check.text == "Мужской", ">>> Ошибка с выбором пола <<<"
            logger.info("Проверка валидации радио-кнопки мужского пола успешна")
        except Exception as e:
            raise logger.error(f"Проверка валидации радио-кнопки мужского пола НЕ успешна {e}")
        


    def redact_company_info(self):
        """ Редактирование полей 'Компания' """
        try:
            logger.info("Нажатие кнопки редактирование полей 'Компания' ")
            self.visibility_of_elements(
            (By. CLASS_NAME, "cursor-pointer")
            )[3].click()
            logger.info("Кнопка редактирования нажата")
        except Exception as e:
            raise logger.error(f"Не удалось нажать кнопку редактирования полей 'Компания'")

    
    def redact_position_info(self):
        """ Редактирования поля 'Должность' """
        try:
            logger.info("Клик по полю 'Должность'"
            "и выбор должности из выпадающего списка")
            self.visibility_of_elements(
            (By. CLASS_NAME, "select__input-container")
            )[0].click()

            logger.info("Выбор первого элемента из выпадающего списка")
            self.element_to_be_clickable(
            (By.CLASS_NAME, "select__menu-list ")
            ).click()
            logger.info("Выбран первый элемент выпадающего списка")
        except Exception as e:
            raise logger.error(f"Не удалось выбрать элемент из выпадающего списка 'Должность'")

    
    def redact_departament_info(self):
        """ Редактирование поля 'Департмаент' """
        try:
            logger.info("Открытие выпадающего списка 'Департамент' ")
            self.visibility_of_elements(
            (By. CLASS_NAME, "select__input-container")
            )[1].click()    

            logger.info("Выбор второго элемента из выпадающего списка")
            self.visibility_of_elements(
            (By. CLASS_NAME, "select__option")
            )[1].click()
            logger.info("Выбран второй элемент выпадающего списка 'Департамен'")
        except Exception as e:
            raise logger.error(f"Не удалось выбрать элемент из выпадающего списка 'Департамент'")

    def redact_head_of_department(self):
        """ Редактирование поля 'Руководитель' """
        try:
            logger.info("Открытие выпадающего списка 'Руководитель'")
            self.visibility_of_elements(
            (By. CLASS_NAME, "select__input-container")
            )[2].click()

            logger.info("Выбор второго элемента из выпадающего списка 'Руководитель'")
            self.visibility_of_elements(
            (By. CLASS_NAME, "select__option")
            )[1].click()
            logger.info("Выбран второй элемент выпадающего списка 'Руководитель'")
        except Exception as e:
            raise logger.error(f"Не удалось выбрать элемент из выпадающего списка 'Руководитель'")

