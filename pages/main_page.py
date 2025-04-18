import time
import random
from utils.logger import Logger
from pages.base_page import BasePage
from utils.main_page_locators import LocatorsMainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


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
        """Вход в случайный канал """
        try:
            logger.info("Выбор канала")
            channels = self.wait_elements(self.locators.ALL_CHANNELS)

            while True:
                channel = random.choice(channels)
                if channel.text.strip() != "Обсуждения":
                    channel.click()
                    logger.info(f"Выбран канал: {channel.text.strip()}")
                    break
                    
        except Exception as e:
            raise logger.error(f"Не удалось выбрать канал: {e}")
            
        
            
    def create_channel_button(self):
        try:
            logger.info("Нажатие кнопки 'Создать канал'")
            actions = ActionChains(self.browser)
            actions.move_by_offset(3, 3).click().perform()
            self.wait_elements(self.locators.CREATE_CHANNEL_BUTTON)[1].click()
            logger.info("Кнопка 'Создать канал' нажата")
        except Exception as e:
            raise logger.error(f"Не удалось нажать кнопку 'Создать канал': {e}")
    
    
    def enter_name_channel(self, name_channel):
        """ Создание канала и ввод его названия. """
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
        """ Описание канала """
        
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
        """ Подтверждение создания канала """
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
        """ Клик по названию канала вызывающий модальное окно c информацией o канале и настройками """
        try:
            logger.info("Нажатие на название канала в хедере приложения")
            header_button = self.element_to_be_clickable(
            self.locators.HEADER_BUTTON
            )
            header_button.click()
            logger.info("Успешное нажатие по названию канала в хедере приложения")
        except Exception as e:
            raise logger.error(f"Не удалось нажать на название канала в хедере приложения: {e}")



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
            raise logger.error(f"Не удалось нажать на вкладку настройки в модальном окне канала: {e}")


    def delete_channel(self):
        """Удаление канала."""
        logger.info("Удаление канала")
        try:
            logger.info(f"Нажатие кнопки 'Удалить канал'")
            delete_button = self.element_to_be_clickable(
                self.locators.DELETE_BUTTON
            )
            delete_button.click()
            logger.info("Ожидания появления модального окна с подтверждением удаления")
            self.visibility_of_elements(
                self.locators.MODAL_NOTIFICATIONS
            )[-1]
            logger.info(f"Подтверждение удаления канала")
            confirm_delete_button = self.element_to_be_clickable(
                self.locators.CONFIRM_DELETE_BUTTON
            )
            confirm_delete_button.click()
            logger.info("Кнопка подтверждения удаления канала нажата")
            self.invis_of_element(self.locators.CONFIRM_DELETE_BUTTON)
        except Exception as e:
            raise logger.error(f"Не удалось удалить канал: {e}")


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
            raise logger.error(f"He удалось архивировать канал: {e}")



    def button_all_archive_channels(self):
        """ Просмотр всех архивных каналов  """
        try:
            logger.info("Нажатие по тоглу с тремя точками")
            self.element_to_be_clickable(self.locators.KEBAB_MENU).click()
            
            logger.info("Успешное нажатие по тоглу с тремя точками")

            logger.info("Просмотр всех архивных каналов")
            self.visibility_of_elements(self.locators.ALL_ARCHIVE_CHANNELS)[1].click()
            
            
            logger.info("Успешное нажатие по кнопке 'Архив'")
        except Exception as e:
            raise logger.error(f"Не удалось нажать по кнопке 'Архив': {e}")




    def main_logo(self):
        """Стрелочка назад"""
        self.visibility_of_element(
            self.locators.MAIN_LOGO
        ).click()




    def waiting_for_modal_window_to_close(self):
        """ Ожидание закрытия модального окна """
        self.invis_of_element(
                self.locators.MODAL_WINDOW
        )

    def waiting_notifications_delete_close(self):
        """ Ожидание закрытия модального окна удаления """
        self.invis_of_element(
            self.locators.DELETE_CONFIRMATION_MESSAGE
        )



    def write_a_message(self, random_message_text):
        """Написание сообщения в созданный канал."""
        try:
            logger.info(f"Попытка ввода сообщения: '{random_message_text}' ")
            message_input = self.visibility_of_element(
                self.locators.MESSAGE_INPUT
            )
            message_input.send_keys(random_message_text)
            logger.info(f"Сообщение: '{random_message_text}' введено")
            
        except Exception as e:
            raise logger.error(f"Не удалось отправить сообщение: {random_message_text},  {e}")



    def write_a_wessage_with_link(self):
        """ Написание сообщения с ссылкой в тексте """
        try:
            
            logger.info("Отправка сообщения с ссылкой")
            self.visibility_of_element(
                self.locators.MESSAGE_INPUT
            ).send_keys(self.locators.SAMPLE_LINK) 
            self.send_message()
            logger.info("Сообщение со ссылкой отправлено")
            messages = self.visibility_of_elements(
                self.locators.LAST_MESSAGE
            )

            message = messages[-1] # Выбор последнего сообщения
            
            action = ActionChains(self.browser)
            action.move_to_element(message).perform()

            self.visibility_of_element(
                self.locators.LINKS_PREVIEV_MESSAGE
            )
            logger.info('Превью ссылки отображается в сообщении')
        except Exception as e:
            logger.error(f"Не удалось проверить отображение линка в сообщении {e}") 


    def edit_last_message(self, edit_message):
        """Редактирование последнего отправленного сообщения"""
        try:
            self.scroll_chat_to_bottom()
            logger.info("Выбор последнего сообщения в чате для редактирования")
            messages = self.visibility_of_elements(self.locators.LAST_MESSAGE)
            if not messages:
                raise Exception("Не найдено сообщений для редактирования")
            
            message = messages[-1]  # Выбор последнего сообщения
           
            action = ActionChains(self.browser)
            logger.info("Навод курсора на последнее сообщение")
            action.move_to_element(message).pause(1).perform()
            
            logger.info("Ожидание кнопки меню сообщения")
            self.wait_elements(self.locators.MESSAGE_MENU)
            
            
            logger.info("Нажатие 'Редактировать сообщение'")

            edit_button = self.wait_elements(self.locators.EDIT_MESSAGE)[-1]
            edit_button.click()

            logger.info("Ожидание модального окна редактирования")
            self.visibility_of_element(self.locators.EDIT_MESSAGE_MODAL)
            

            logger.info("Очистка поля ввода")
            write_message = self.visibility_of_element(self.locators.MESSAGE_FIELD)
            write_message.clear() 
            
            logger.info("Ввод нового текста")
            write_message.send_keys(edit_message)
            logger.info("Сообщение отредактировано")
            self.scroll_chat_to_bottom()

        except Exception as e:
            raise logger.error(f"Ошибка редактирования сообщения: {e}")
           



    def reply_message(self, rand_reply):
        """ Ответ на сообщение """
        try:
            self.scroll_chat_to_bottom()
            logger.info("Ответ на сообщение")
            messages = self.visibility_of_elements(
                self.locators.LAST_MESSAGE
            )        
            message = messages[-1] # Выбор последнего сообщения
            
            action = ActionChains(self.browser)
            action.move_to_element(message).perform()

            reply_message_button = self.wait_elements(
                self.locators.REPLY_MESSAGE
            )[-1]
            logger.info("Нажатие по кнопке 'ответить на сообщение'")
            action.click(reply_message_button).perform()
            logger.info("Успешное нажатие по кнопке 'ответить на сообщение'")

            logger.info("Ожидание появления модального окна ответа на сообщения над полем ввода")
            self.visibility_of_element(self.locators.MODAL_REPLY)
            logger.info("Модальное окно успешно появилось")

            self.visibility_of_element(self.locators.MESSAGE_INPUT)
            logger.info('Ввод ответа на сообщение в поле ввода')

            self.element_to_be_clickable(
                self.locators.MESSAGE_INPUT
            ).send_keys(rand_reply)
        
        except Exception as e:
            raise logger.error(f"Ошибка ответа на сообщение {e}")
            




    def send_message(self):
        """ Кнопка отправки сообщения """
        try:
            logger.info("Нажатие кнопки 'Отправить сообщение'")
            send_button = self.element_to_be_clickable(
                self.locators.SEND_MESSAGE_BUTTON
            )
            send_button.click()
            logger.info("Сообщение отправлено")
        except Exception as e:
            raise logger.error(f"Сообщение не отправлено")

    def send_message_user(self, random_message_text):
        """ Кнопка отправки сообщения """
        try:    
            logger.info("Нажатие кнопки 'Отправить сообщение'")
            self.element_to_be_clickable(
                self.locators.SEND_MESSAGE_BUTTON).click()
            
            
            self.invis_of_element(self.locators.SEND_MESSAGE_BUTTON)

            messages = self.visibility_of_elements(self.locators.LAST_MESSAGE)[-1]
            messages = messages.text
                
            for _ in range (5):
                if messages == random_message_text:
                    logger.info("Сообщение отправлено")
                    break 
        except Exception as e:
            raise logger.error(f"Сообщение не отправлено {e}")
        


    

    def other_actions(self, max_attempts=3):
        """Кнопки действий для сообщений с попытками для разных сообщений"""
        self.scroll_chat_to_bottom()
        
        for attempt in range(max_attempts):
            try:
                logger.info(f"Попытка {attempt + 1} из {max_attempts}")
            
                messages = self.wait_elements(self.locators.LAST_MESSAGE)
                if not messages:
                    raise Exception("Не найдено сообщений в чате")
                
                message_idx = -1 - attempt
                if abs(message_idx) > len(messages):
                    message_idx = -1  
                    
                message = messages[message_idx]
                logger.info(f"Выбрано сообщение {len(messages) + message_idx + 1} из {len(messages)}")
                
               
                
                action = ActionChains(self.browser)
                action.move_to_element(message).pause(1).perform()
                
                other_buttons = self.wait_elements(self.locators.OTHER_ACTIONS)
               
                if other_buttons:
                    try:
                        other_buttons[-1].click()
                        logger.info("Меню действий успешно открыто")
                        return True
                    except Exception as btn_error:
                        logger.error(f"Ошибка клика: {str(btn_error)}. Пробуем следующее сообщение...")
                        continue
                
            except Exception as e:
                logger.error(f"Ошибка в попытке {attempt + 1}: {str(e)}")
                if attempt == max_attempts - 1:
                    raise Exception(f"Не удалось выполнить действие после {max_attempts} попыток")
                continue
        return False



    def delete_message(self):
        self.scroll_chat_to_bottom()
        logger.info("Удаление сообщения")
        
        element = self.visibility_of_elements(
            self.locators.DELETE_MESSAGE
        )[-1]

        
        element.click()

        self.visibility_of_element(
            self.locators.MODAL_NOTIFICATIONS)

        logger.info("Подтверждение удаления сообщения")
        self.element_to_be_clickable(
            self.locators.CONFIRM_DELETE_MESSAGE
        ).click()
        logger.info("Ожидание появления карточки с удаленным сообщением")
        self.visibility_of_elements(
            self.locators.DELETE_CHECK)
        self.invis_of_element(
            self.locators.DELETE_CHECK)
        logger.info("Карточка с удаленным сообщением появилась")
        

    def open_discussions_and_write_message(self, disc_message, max_attempts=3):
        """Cоздание обсуждения и отправка сообщения"""
        for attempt in range(max_attempts):
            try:
                logger.info(f"Попытка {attempt + 1} из {max_attempts}")
                
                
                messages = self.visibility_of_elements(self.locators.LAST_MESSAGE) 
                message = messages[-1 - (attempt % len(messages))]  
                
               
                ActionChains(self.browser).move_to_element(message).pause(1).perform()
                    # 10,  # Смещение по X 
                    # 10   # Смещение по Y
                
                
                
                btn = self.wait_elements(
                    self.locators.DISCUSSIONS_BUTTON)[-1]
                
               
                if btn.is_displayed():
                    btn.click()
                else:
                    raise Exception("Кнопка не видна")

                logger.info("Ожидание появления модального окна с обсуждением")
                self.visibility_of_element(
                    self.locators.DISCUSSIONS_MODAL)
                logger.info("Модальное окно успешно появилось")

                logger.info("Ввод сообщения в обсуждение ")
                self.visibility_of_element(
                    self.locators.DISCUSSIONS_MESSAGE
                ).send_keys(disc_message)

                send = self.element_to_be_clickable(
                    self.locators.SEND_MESSAGE_BUTTON
                )
                send.click()
                logger.info("Сообщение написано и отправлено")

                logger.info("Закрытие обсуждения кликом по крестику")
                close = self.element_to_be_clickable(
                    self.locators.DISCUSSIONS_MODAL_CLOSE
                )
                close.click()
                logger.info("Обсуждение закрыто")

                logger.info("Проверка отображение обсуждений под сообщением")
                self.visibility_of_elements(
                    self.locators.DISCUSSIONS_UNDER_MESSAGE
                )[0]
                logger.info("Обсуждения отображаются под сообщением")    
               
                return True
                
            except Exception as e:
                logger.error(f"Ошибка в попытке {attempt + 1}: {str(e)}")
                if attempt == max_attempts - 1:
                    raise Exception(f"Не удалось после {max_attempts} попыток")


    def decline_notifications(self):
        """ Ожидание и нажатие кнопки 'Отклонить уведомления' """

        try:
            logger.info("Ожидание появления модального окна")
            self.visibility_of_element(self.locators.MODAL_NOTIFICATIONS)
            logger.info("Появилось окно с уведомлениями")
            logger.info("Нажатие кнопки 'Отклонить уведомления'")                
            self.element_to_be_clickable(self.locators.DECLINE_NOTIFICATIONS_BUTTON
            ).click()
            logger.info("Кнопка 'Отклонить уведомления' нажата")
        except Exception as e:
            raise logger.error(f"Не удалось нажать кнопку 'Отклонить уведомления': {e}")


    def create_message(self):
        """ Нажатие по плюсику Написать сообщение """
        try:
            logger.info("Нажатие по плюсику написать сообщение")
            self.wait_elements(
                self.locators.CREATE_MESSAGE_BUTTON
            )[2].click()
            logger.info("Нажатие по плюсику успешно")
        except Exception as e:
            raise logger.error(f"Не удалось нажать по плюсику Написать сообщение {e}")

    def user_search_and_selection(self, user):
        """ Поиск юзера в поле ввода 'Кому' """
        try:
            logger.info(f"Поиск юзера '{user}' в поле ввода 'Кому' ")
            self.visibility_of_element(
                self.locators.SEARCH_USER
            ).send_keys(user)
            logger.info(f"Введено имя пользователя: '{user}' ")

            logger.info(f"Выбор пользователя: {user}")
            self.element_to_be_clickable(
                self.locators.SELECT_USER
            ).click()
            logger.info(f"Выбран пользователь: {user}")
            actions = ActionChains(self.browser)
            actions.move_by_offset(10, 10).click().perform()
        except Exception as e:
            raise logger.error(f"Не удалось выбрать пользователя: '{user}' ")


    def select_first_user(self):
        """ Выбор первого пользователя во вкладке Сообщения """
        try:
            logger.info("Выбор первого пользователя во вкладке Сообщения")
            self.visibility_of_elements(
                self.locators.SELECT_USER_FROM_LIST)[0].click()
            actions = ActionChains(self.browser)
            actions.move_by_offset(3, 3).click().perform()
        except Exception as e:
            raise logger.error(f"Не удалось выбрать пользователя")

    def check_channel_deleted(self, channel_name):
        """Проверяет, что канала нет в списке"""
        for _ in range(5):  
            channels = self.wait_elements(self.locators.CHANNELS_LIST)
            
            if not channels or not any(ch.text == channel_name for ch in channels):
                logger.info(f"Канал '{channel_name}' удален")
                return True
                
        
        logger.error(f"Ошибка: канал '{channel_name}' не удален")
        return False
        
    def message_deletion_check(self, random_message_text):
        """Проверка удаления сообщения"""
        try:
            elements = self.wait_elements(
                self.locators.MESSAGE_TEXT
            )
            
            found = False
            for element in elements:
                if random_message_text in element.text:
                        found = True
                        break
                if found:
                    raise Exception(f"Сообщение ' {random_message_text}' не было удалено.")
                else:
                    logger.info(f"Сообщение ' {random_message_text}' успешно удалено.")
                    self.scroll_chat_to_bottom_instantly()
        except Exception as e:
                raise logger.error(f"Не удалось проверить удаление сообщения: {e}")
                
        
    def check_reply_message(self):
        self.scroll_chat_to_bottom()
        logger.info('Проверка появления ответа на сообщение')
        self.visibility_of_elements(
            self.locators.CHECK_REPLY
        )[-1]
        logger.info('Успешное появления ответа на сообщение')
       

    def check_edit_message(self, edit_message):
        try:
            self.scroll_chat_to_bottom()
            logger.info("Проверка отредактированного сообщения")
            messages = self.visibility_of_elements(
                self.locators.LAST_MESSAGE)
            
            message = messages[-1]
            assert message.text == edit_message, "<<<<<<<<< edited message, error >>>>>>>>>>"
            logger.info("Проверка успешна")
        except Exception as e:
            raise logger.error(f"Не удалось проверить отредактированное сообщение {e}")   




    def archive_channel_check(self, name_channel):
        """Проверка всех Архивных каналов"""
        logger.info(f"Проверка присутствия канала: {name_channel} в Архиве")
        try:
            
            channel_list = self.visibility_of_elements(self.locators.CHANNELS_LIST)
            
            
            for channel in channel_list:
                if channel.text == name_channel:
                    logger.info(f"Канал {name_channel} найден в Архиве")
                    return  
            
            logger.error(f"Канал {name_channel} отсутствует в Архиве")

        except Exception as e:
            raise logger.error(f"Не удалось проверить архивирование канала: {name_channel}, {e}")


    def archive_channel_notifications_check(self):
        """Проверка уведомления об архивировании канала"""
        try:    
            logger.info("Проверка уведомления об архивировании канала")
            check = self.visibility_of_element(self.locators.DELETE_CONFIRMATION_MESSAGE)
            assert check.text == "Изменения сохранены", ">>> Не удалось проверить архивирование канала"
            logger.info("Уведомление об архивировании канала успешно проверено")
            self.invis_of_element(self.locators.DELETE_CONFIRMATION_MESSAGE)
        except Exception as e:
            logger.error(f"Не удалось проверить уведомление об архивировании канала: {e}")



    def delete_channel_notifications_check(self):
        """Проверка уведомления об удалении канала"""
        logger.info("Проверка уведомления об удалении канала")
        try:
            check = self.visibility_of_element(self.locators.DELETE_CONFIRMATION_MESSAGE)
            assert check.text == "Канал удален", ">>> Не удалось проверить уведомление об удалении канала"
            logger.info("Уведомление об удалении канала успешно проверено")
            
        except Exception as e:
            
            logger.error(f"Не удалось проверить уведомление об удаление канала: {e}")

        
    def check_message(self, random_message_text):
        """ Проверка отправки сообщения """
        try:
            message = self.visibility_of_elements(
                self.locators.MESSAGE_TEXT
            )[1]
            logger.info(f"Первая попытка проверки отправки сообщения:")
            assert (
                message.text == random_message_text
        
            ), ">>> Message assert ERROR, first try<<<"
        except Exception as e:
            logger.info(f"Вторая попытка проверки отправки сообщения: {e}")
            message = self.visibility_of_elements(
                self.locators.MESSAGE_TEXT
            )[1]
            assert (
                message.text == random_message_text
        
            ), ">>> Message assert ERROR, second try, message not found<<<"

    def check_last_send_message(self, random_message_text):
        self.scroll_chat_to_bottom_instantly()
        time.sleep(1)
        found = False
        for _ in range(10):
            messages = self.visibility_of_elements(
                self.locators.LAST_MESSAGE)
            if messages and messages[-1].text == random_message_text:
                found = True
                logger.info(f"Сообщение '{random_message_text}' найдено ")
                break
            
        actions = ActionChains(self.browser)
        actions.click(messages[-1]).perform()
        if not found:
            raise AssertionError(f"Текст '{random_message_text}' не найден")







    