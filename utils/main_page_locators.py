from selenium.webdriver.common.by import By   


class LocatorsMainPage:

    MESSAGE_FIELD = (By.CSS_SELECTOR, '[aria-owns="quill-mention-list"]')

    CREATE_CHANNEL_BUTTON = (By.CLASS_NAME, 'sphr-button__icon') # [1]
    CHANNEL_NAME_FIELD = (By.ID, "name")
    CHANNEL_INFO_FIELD = (By.ID, "description")
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Продолжить']")
    ALL_CHANNELS = (By. CLASS_NAME, "spheraui-block-field__text-container")
    BACK_ARROW = (By. CLASS_NAME, "sc-ckEbSK.bISGyO")

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
    KEBAB_MENU = (By.CLASS_NAME, 'sphr-button__icon') # [0]
    ALL_ARCHIVE_CHANNELS = (By. CLASS_NAME, "spheraui-menu-item--secondary") #[1]



    CHANNELS_LIST = (By.CSS_SELECTOR, '[class="spheraui-block-field__text"]')


    MESSAGE_INPUT = (By.CLASS_NAME, "ql-editor")
    SEND_MESSAGE_BUTTON = (By.CLASS_NAME, 'send-button__active')
    MESSAGE_TEXT = (By.CLASS_NAME, "message-text")
    # MESSAGE_MENU = (By.CLASS_NAME, "message-action-buttons-container")
    LAST_MESSAGE = (By.CSS_SELECTOR, "div > .message-text") #[-1]

    ALL_MESSAGES_IN_CHANNEL = (By.CSS_SELECTOR, ".message-card > .message-text > p")
    MESSAGE_MENU = (By.CLASS_NAME, "message-action-buttons-container")
    OTHER_ACTIONS = (By.CSS_SELECTOR, '[aria-label="Другие действия"]')
    EDIT_MESSAGE = (By.CSS_SELECTOR, '[aria-label="Редактировать сообщение"]')
    REPLY_MESSAGE = (By.CSS_SELECTOR, '[aria-label="Ответить на сообщение"]')
    MODAL_REPLY = (By. CLASS_NAME, "sc-hpfkCd.hFJVdA")
    DELETE_MESSAGE = (By. CLASS_NAME, "spheraui-menu-item--secondary") # [-1]
    CONFIRM_DELETE_MESSAGE = (By. CLASS_NAME, "error-button")

    LINKS_PREVIEV_MESSAGE = (By. CLASS_NAME, "link-previews__preview")
    EDIT_MESSAGE_MODAL = (By. CLASS_NAME, "action-message__icon-container")
    MODAL_NOTIFICATIONS = (By.CLASS_NAME, "MuiDialog-paperFullWidth")
    LINKS_PREVIEV_MESSAGE = (By. CLASS_NAME, "link-previews__preview")
    DECLINE_NOTIFICATIONS_BUTTON = (By. CLASS_NAME, "MuiButton-outlinedSizeMedium")
