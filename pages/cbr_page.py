from pages.base_page import BasePage
from locators import CBRPageLocators, CBRReceptionPageLocators, CBRReceptionPageMessageLocators, CBRAboutWarningPageLocators


class CBRPage(BasePage):
    def site_map_button_click(self):
        button = self.browser.find_element(*CBRPageLocators.MENU_BUTTON)
        button.click()

    def site_map_about_click(self):
        button = self.browser.find_element(*CBRPageLocators.MENU_ABOUT_BUTTON)
        button.click()

    def site_map_about_warning_click(self):
        button = self.browser.find_element(*CBRPageLocators.MENU_ABOUT_WARNIN_BUTTON)
        button.click()

    def reception_click(self):
        button = self.browser.find_element(*CBRPageLocators.RECEPTION_BUTTON)
        button.click()

    def en_language_click(self):
        button = self.browser.find_element(*CBRPageLocators.EN_LANGUAGE_BUTTON)
        button.click()


class CBRReceptionPage(CBRPage):
    def write_thanks_click(self):
        button = self.browser.find_element(*CBRReceptionPageLocators.WRITE_THANKS_BUTTON)
        button.click()


class CBRReceptionMessagePage(CBRPage):
    def enter_thanks_message(self, text:str):
        field = self.browser.find_element(*CBRReceptionPageMessageLocators.MESSAGE_FIELD)
        field.send_keys(text)

    def agreement_flag_click(self):
        flag = self.browser.find_element(*CBRReceptionPageMessageLocators.AGREEMENT_CHECKBOX)
        flag.click()

    def getScreenshot(self) -> bytes:
        form = self.browser.find_element(*CBRReceptionPageMessageLocators.MESSAGE_FORM)
        return form.screenshot_as_png


class CBRAboutWarningPage(CBRPage):
    def getWarningText(self):
        header = self.browser.find_element(*CBRAboutWarningPageLocators.HEADER_TEXT).text
        body = self.browser.find_element(*CBRAboutWarningPageLocators.BODY_TEXT).text
        return(header, body)


