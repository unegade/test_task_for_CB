from selenium.webdriver.common.by import By


class GoogleStartPageLocators():
    SEARCH_FIELD = (By.NAME, 'q')
    SEARCH_IN_HINT_BUTTON = (By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
    SEARCH_GENERAL_BUTTON = (By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')


class CBRPageLocators():
    BASE_ADDRESS = 'www.cbr.ru'
    EN_LANGUAGE_BUTTON = (By.XPATH, '//*[@id="layout"]/div[1]/div[2]/div/ul/li[2]/a')
    MENU_BUTTON = (By.CLASS_NAME, 'burger')
    RECEPTION_BUTTON = (By.PARTIAL_LINK_TEXT, 'Интернет-приемная')
    MENU_ABOUT_BUTTON = (By.LINK_TEXT, 'О сайте')
    MENU_ABOUT_WARNIN_BUTTON = (By.LINK_TEXT, 'Предупреждение')


class CBRReceptionPageLocators():
    WRITE_THANKS_BUTTON = (By.XPATH, '//*[@id="content"]/div[1]/div[3]/a')


class CBRReceptionPageMessageLocators():
    MESSAGE_FIELD = (By.ID, 'MessageBody')
    AGREEMENT_CHECKBOX = (By.ID, '_agreementFlag')
    MESSAGE_FORM = (By.ID, '_wizardForm')


class CBRAboutWarningPageLocators():
    HEADER_TEXT = (By.XPATH, '//*[@id="main"]/h1/span')
    BODY_TEXT = (By.XPATH, '//*[@id="content"]/p')