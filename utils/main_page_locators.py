from selenium.webdriver.common.by import By   


class LocatorsMainPage:
    CREATE_CHANNEL_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Создать канал"]')
    CHANNEL_NAME_FIELD = (By.ID, "name")
    CHANNEL_INFO_FIELD = (By.ID, "description")
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Продолжить']")
    ALL_CHANNELS = (By. CLASS_NAME, "channel-data-container")


    HEADER_BUTTON = (By.CLASS_NAME, "header__button")
    MODAL_WINDOW = (By.CLASS_NAME, "dialog__paper")
    SETTINGS_TAB = (By.CSS_SELECTOR, '[role="tab"]')
    DELETE_BUTTON = (By.CLASS_NAME, "settings__button-warning")
    CONFIRM_DELETE_BUTTON = (By.CLASS_NAME, "error-button")
    DELETE_CONFIRMATION_MESSAGE = (
        By.CSS_SELECTOR,
        ".Toastify__toast-body > div:nth-child(2)",
    )
    ARCHIVE_CHANNEL = (By. CLASS_NAME, "settings__button")
    ARCHIVE_CONFIRM_BUTTON = (By.CLASS_NAME, "error-button")


    MESSAGE_INPUT = (By.CLASS_NAME, "ql-editor")
    SEND_MESSAGE_BUTTON = (By.CLASS_NAME, 'send-button__active')
    MESSAGE_TEXT = (By.CLASS_NAME, "message-text")

    ALL_MESSAGES_IN_CHANNEL = (By.CSS_SELECTOR, ".message-card > .message-text > p")
    MESSAGE_MENU = (By.CLASS_NAME, "message-action-buttons-container")
    OTHER_ACTIONS = (By.CSS_SELECTOR, 'button[aria-label="Другие действия"]')
    DELETE_MESSAGE = (By. CLASS_NAME, "menu-item")
    CONFIRM_DELETE_MESSAGE = (By. CLASS_NAME, "error-button")


    MODAL_NOTIFICATIONS = (By.CLASS_NAME, "MuiDialog-paperFullWidth")
    DECLINE_NOTIFICATIONS_BUTTON = (By. CLASS_NAME, "MuiButton-outlinedSizeMedium")
