from selenium.webdriver.common.by import By   


class LocatorsMainPage:

    SCROLL_CHAT = (By.CLASS_NAME, "virtual-list__scroll-container")

    SEARCH_USER = (By. CLASS_NAME, "search-string-input")
    SELECT_USER = (By. CLASS_NAME, "user-option-item")
    SELECT_USER_FROM_LIST = (By. CLASS_NAME, "spheraui-block-field__avatar-info")

    MESSAGE_INPUT = (By.CLASS_NAME, "ql-editor")
    MESSAGE_FIELD = (By.CSS_SELECTOR, '[aria-owns="quill-mention-list"]')
    
    CREATE_MESSAGE_BUTTON = CREATE_CHANNEL_BUTTON = (By.CLASS_NAME, "sphr-button__icon") # [2]
    SEND_MESSAGE_BUTTON = (By.CLASS_NAME, 'send-button__active')
    SEND_MESSAGE_DISCUSSIONS = (By. CLASS_NAME, "iSasNz")
    
    MESSAGE_TEXT = (By.CLASS_NAME, "message-text")
    LAST_MESSAGE = (By.CSS_SELECTOR, "div > .message-text") #[-1]
    ALL_MESSAGES_IN_CHANNEL = (By.CSS_SELECTOR, ".message-card > .message-text > p")
    ALL_MESSAGES_WITH_USER = (By.CSS_SELECTOR, ".message-card > .message-text")

    
    MESSAGE_MENU = (By.CLASS_NAME, "message-action-buttons-container")

    EDIT_MESSAGE = (By.CSS_SELECTOR, '[aria-label="Редактировать сообщение"]')
    EDIT_MESSAGE_MODAL = (By. CLASS_NAME, "action-message__icon-container")

    REPLY_MESSAGE = (By.CSS_SELECTOR, '[aria-label="Ответить на сообщение"]')
    MODAL_REPLY = (By. CLASS_NAME, "sc-hpfkCd.hFJVdA")
    CHECK_REPLY = (By. CLASS_NAME, "sc-eVZGIO.kgVmpG")


    OTHER_ACTIONS = (By.CSS_SELECTOR, '[aria-label="Другие действия"]')
    DELETE_MESSAGE = (By. CLASS_NAME, "spheraui-menu-item--secondary") # [-1]
    CONFIRM_DELETE_MESSAGE = (By. CLASS_NAME, "error-button")
    DELETE_CHECK = (By. CLASS_NAME, "message__message-deleted")

    DISCUSSIONS_BUTTON = (By. CSS_SELECTOR, '[aria-label="Начать обсуждение"]')
    DISCUSSIONS_MESSAGE = (By. CSS_SELECTOR, '[data-placeholder="Ответить в обсуждение"]')
    DISCUSSIONS_MODAL = (By. CLASS_NAME, "thread-content-container")
    DISCUSSIONS_MODAL_CLOSE = (By. CLASS_NAME, "thread-close-button")
    DISCUSSIONS_UNDER_MESSAGE = (By. CLASS_NAME, "hrpeaa")

    CREATE_CHANNEL_BUTTON = (By.CLASS_NAME, "sphr-button__icon") # [1]
    CHANNEL_NAME_FIELD = (By.ID, "name")
    CHANNEL_INFO_FIELD = (By.ID, "description")
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Продолжить']")


    ALL_CHANNELS = (By. CLASS_NAME, "spheraui-block-field__text-container")
    BACK_ARROW = (By. CLASS_NAME, "sc-ckEbSK.bISGyO")
    CHANNELS_LIST = (By.CSS_SELECTOR, '[class="spheraui-block-field__text"]')

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
    LINKS_PREVIEV_MESSAGE = (By. CLASS_NAME, "link-previews__preview")
    MODAL_NOTIFICATIONS = (By.CLASS_NAME, "MuiDialog-paperFullWidth")

    LINKS_PREVIEV_MESSAGE = (By. CLASS_NAME, "link-previews__preview")
    DECLINE_NOTIFICATIONS_BUTTON = (By. CLASS_NAME, "MuiButton-outlinedSizeMedium")


    SAMPLE_LINK = "https://xn--80abh7bk0c.xn--p1ai/quote/432352"
