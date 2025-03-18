from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
from utils.main_page_locators import LocatorsMainPage
from utils.logger import Logger
from pages.base_page import BasePage


logger = Logger()




class MainPage(BasePage):
    def __init__(self, browser):
        """Инициализация класса.

        Объект браузера (WebDriver).
        """
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)
        self.locators = LocatorsMainPage
        super(MainPage, self).__init__(browser)




    def enter_in_random_channel(self):
        """ Вход в рандомный канал """
        try:
            logger.info("Выбор рандомного канала")
            self.visibility_of_element(self.locators.ALL_CHANNELS)
            channel = self.wait_elements(self.locators.ALL_CHANNELS)[1::]
            random_channel = random.choice(channel)
            logger.info(f"Выбран канал: {random_channel.text}")
            random_channel.click()
            logger.info(f"Вход в канал {random_channel.text}")
        except Exception as e:
            logger.error(f"Не удалось выбрать канал: {e}")
        
            
    def create_channel_button(self):
        try:
            logger.info("Нажатие кнопки 'Создать канал'")
            create_channel_button = self.element_to_be_clickable(
            self.locators.CREATE_CHANNEL_BUTTON
            )
            create_channel_button.click()
            logger.info("Кнопка 'Создать канал' нажата")
        except Exception as e:
            logger.error(f"Не удалось нажать кнопку 'Создать канал': {e}")
    
    
    def enter_name_channel(self, name_channel):
        """Создание канала и ввод его названия. """
        try:
            logger.info("Ожидание появления модального окна")
            self.element_to_be_clickable(self.locators.MODAL_WINDOW)
            logger.info(f"Ввод названия канала")
            channel_name_field = self.wait_element(
                self.locators.CHANNEL_NAME_FIELD
            )
            channel_name_field.send_keys(name_channel)
            logger.info(f"Название канала '{name_channel}' введено")
        except:
            logger.info("Не удалось ввести название канала с первого раза, перезапуск")
            channel_name_field = self.visibility_of_element(
                self.locators.CHANNEL_NAME_FIELD
            )
            channel_name_field.send_keys(name_channel)
            logger.info(f"Название канала '{name_channel}' введено")
            


    def channel_info(self, info_channel):
        """
        Описание канала
        """
        
        try:
            logger.info(f"Ввод описания канала {info_channel} ")
            channel_info_field = self.visibility_of_element(
                self.locators.CHANNEL_INFO_FIELD
            )
            channel_info_field.send_keys(info_channel)
            logger.info(f"Описание канала '{info_channel}' введено")
        except Exception as e:
            logger.error(f"Не удалось ввести описание канала {e}")


    def channel_creation_confirmation_button(self):
        """
        Подтверждение создания канала
        """
        try:
            logger.info(
            "Нажатие кнопки 'продолжить' после заполнения всех обязательных полей при создании канала"
        )
            continue_button = self.element_to_be_clickable(
                self.locators.CONTINUE_BUTTON
            )
            continue_button.click()
            logger.info("Канал успешно создан")
        except Exception as e:
            logger.error(f"Канал не создан {e}")

    def header_button_channel(self):
        """ Клик по названию канала
        вызывающий модальное окно
        c информацией o канале и настройками
        """
        try:
            logger.info("Нажатие на название канала в хедере приложения")
            header_button = self.element_to_be_clickable(
            self.locators.HEADER_BUTTON
            )
            header_button.click()
            logger.info("Успешное нажатие по названию канала в хедере приложения")
        except Exception as e:
            logger.error(f"Не удалось нажать на название канала в хедере приложения: {e}")



    def settings_tab_in_modal_window(self):
        """ Вкладка настройки в модальном окне """
        try:
            logger.info("Вкладка настройки в модальном окне")
            settings_tab = self.wait_elements(
                self.locators.SETTINGS_TAB
            )[2]
            settings_tab.click()
            logger.info("Успешное нажатие по вкладке настройки в модальном окне канала")
        except Exception as e:
            logger.error(f"Не удалось нажать на вкладку настройки в модальном окне канала: {e}")


    def delete_channel(self):
        """Удаление канала."""
        logger.info("Удаление канала")
        try:
            logger.info(f"Нажатие кнопки 'Удалить канал'")
            delete_button = self.element_to_be_clickable(
                self.locators.DELETE_BUTTON
            )
            delete_button.click()
            logger.info(f"Подтверждение удаления канала")
            confirm_delete_button = self.element_to_be_clickable(
                self.locators.CONFIRM_DELETE_BUTTON
            )
            confirm_delete_button.click()
            logger.info("Канал успешно удален")
        except Exception as e:
            logger.error(f"Не удалось удалить канал: {e}")


    def archive_channel(self):
        """ Архивирование канала."""
        logger.info("Архивирование канала")
        try:
            logger.info("Нажатие кнопки 'Архивировать канал'")
            archive = self.visibility_of_elements(self.locators.ARCHIVE_CHANNEL)[0]
            archive.click()
            archive_confirm = self.visibility_of_element(self.locators.CONFIRM_DELETE_BUTTON)
            logger.info("Нажатие кнопки подтверждения")
            archive_confirm.click()
            logger.info("Канал успешно архивирован")
        except Exception as e:
            logger.error(f"He удалось архивировать канал: {e}")


    def delete_channel_notifications_check(self):
        """Проверка уведомления об удалении канала"""
        logger.info("Проверка уведомления об удалении канала")
        try:
            check = self.visibility_of_element(self.locators.DELETE_CONFIRMATION_MESSAGE)
            assert check.text == "Канал удален", ">>> Не удалось проверить удаление канала"
            logger.info("Уведомление об удалении канала успешно проверено")
            
        except Exception as e:
            logger.error(f"Не удалось проверить уведомление об удаление канала: {e}")

    def delete_channel_check(self, name_channel):
        """Проверка удаления канала"""
        logger.info(f"Проверка удаления канала: {name_channel}")
        try:
            self.refresh_page()
            
            channel_list = self.wait_elements((By.CLASS_NAME, "channel-name"))

            # Проверяем каждый канал
            for channel in channel_list:
                if channel.text == name_channel:
                    logger.error(f"Канал {name_channel} не удален")
                    return

            # Если канал не найден в списке
            logger.info(f"Канал {name_channel} успешно удален")
        except Exception as e:
            logger.error(f"Не удалось проверить удаление канала: {name_channel}, {e}")

    def archive_channel_notifications_check(self):
        """Проверка уведомления об архивировании канала"""
        try:    
            logger.info("Проверка уведомления об архивировании канала")
            check = self.visibility_of_element(self.locators.DELETE_CONFIRMATION_MESSAGE)
            assert check.text == "Изменения сохранены", ">>> Не удалось проверить архивирование канала"
            logger.info("Уведомление об архивировании канала успешно проверено")
            # self.invis_of_element(self.locators.DELETE_CONFIRMATION_MESSAGE)
        except Exception as e:
            logger.error(f"Не удалось проверить уведомление об архивировании канала: {e}")
    
    def Waiting_for_modal_window_to_close(self):
        """ Ожидание закрытия модального окна """
        self.invis_of_element(
                self.locators.MODAL_WINDOW
        )


    def write_a_message(self, rand_message):
        """Написание сообщения в созданный канал."""
        try:
            logger.info("Попытка ввода сообщения")
            message_input = self.visibility_of_element(
                self.locators.MESSAGE_INPUT
            )
            message_input.send_keys(rand_message)
            logger.info("Сообщение введено")
        except Exception as e:
            logger.error(f"Не удалось отправить сообщение: {rand_message},  {e}")


    def send_message(self):
        """
        Кнопка отправки сообщения
        """
        try:
            logger.info("Нажатие кнопки 'Отправить сообщение'")
            send_button = self.element_to_be_clickable(
                self.locators.SEND_MESSAGE_BUTTON
            )
            send_button.click()
            logger.info("Сообщение отправлено")
        except Exception as e:
            logger.error(f"Сообщение не отправлено")

    def delete_message(self):
        """ Кнопки действий последнего сообщения в чате """
        try:
            logger.info(f"Наведение курсора на последнее сообщение")
            messages = self.visibility_of_elements(
                (By.CSS_SELECTOR, "div > .message-text"))
            
            message = messages[-1] # Выбор последнего сообщения

            logger.info("Наведение курсора на сообщение")
            action = ActionChains(self.browser)
            action.move_to_element(message).perform()

            self.wait_elements(
               self.locators.MESSAGE_MENU
            )[-1]

            logger.info("Нажатие кнопки 'Другие действия'")
            self.wait_elements(
            self.locators.OTHER_ACTIONS
            )[-1].click()

            logger.info("Удаление сообщения")
            self.visibility_of_elements(
                self.locators.DELETE_MESSAGE
            )[-1].click()

            logger.info("Подтверждение удаления сообщения")
            self.visibility_of_element(
                self.locators.CONFIRM_DELETE_MESSAGE
            ).click()
        except Exception as e:
            logger.error(f"Не удалось удалить сообщение: {e}")

    def check_message(self, rand_message):
        """
        Проверка отправки сообщения
        """
        try:
            message = self.wait.until(
                EC.visibility_of_all_elements_located(self.locators.MESSAGE_TEXT)
            )[1]
            logger.info(f"Первая попытка проверки отправки сообщения:")
            assert (
                message.text == rand_message
            ), ">>> Message assert ERROR, first try<<<"
        except Exception as e:
            logger.info(f"Вторая попытка проверки отправки сообщения: {e}")
            message = self.visibility_of_elements(
                self.locators.MESSAGE_TEXT
            )[1]
            assert (
                message.text == rand_message
            ), ">>> Message assert ERROR, second try, message not found<<<"


    def check_all_messages(self, rand_message):
        """Проверка всех сообщений по тексту"""
        try:
            logger.info("Поиск отправленного сообщения по всем сообщениям")
            elements = self.visibility_of_elements(
                self.locators.ALL_MESSAGES_IN_CHANNEL
            )
            found = False
            for element in elements:
                if rand_message in element.text:
                    found = True
                    logger.info(f"Текст '{rand_message}' найден в элементе: {element.text}")
                    logger.info("Сообщение найдено")
                    break

            if not found:
                logger.info("Сообщение не найдено")
                raise Exception(f"Текст '{rand_message}' не найден ни в одном из элементов.")
            
        except Exception as e:
            logger.error(f"Ошибка: {e}")

    def message_deletion_check(self, rand_message):
        """Проверка удаления сообщения"""
        try:
            elements = self.wait_elements(
                (By.CSS_SELECTOR, ".message-card > .message-text > p"))
            
            found = False
            # Проверка, что сообщение больше не существует
            for element in elements:
                if rand_message in element.text:
                    found = True
                    break

            if found:
                raise Exception(f"Сообщение '{rand_message}' не было удалено.")
            else:
                logger.info(f"Сообщение '{rand_message}' успешно удалено.")
        except Exception as e:
            logger.error(f"Не удалось проверить удаление сообщения: {e}")
            raise

