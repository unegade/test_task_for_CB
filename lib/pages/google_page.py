from selenium.webdriver.support import expected_conditions as EC
from lib.pages.base_page import BasePage
from lib.locators import GoogleStartPageLocators


class GoogleStartPage(BasePage):
    def check_search_field(self):
        search_field = self.browser.find_element(*GoogleStartPageLocators.SEARCH_FIELD)

    def insert_text_in_search_field(self, text: str):
        search_field = self.browser.find_element_by_name('q')
        search_field.send_keys(text)
    
    # !!! Заменить try/except на что-то нормальное !!!
    def click_search_button(self):
        """Т.к. на странице Google 2 кнопки поиска, то жмется видимая."""
        try:
            search_button = self.browser.find_element(*GoogleStartPageLocators.SEARCH_IN_HINT_BUTTON)
            search_button.click()
        except:
            search_button = self.browser.find_element(*GoogleStartPageLocators.SEARCH_GENERAL_BUTTON)
            search_button.click()

    def check_result_link_by_partial_link_text(self, text: str):
        assert len(self.browser.find_elements_by_partial_link_text(text)) > 0

    def go_to_result_link_by_partial_link_text(self, text: str, numbeLink=0):
        links = self.browser.find_elements_by_partial_link_text(text)
        links[numbeLink].click()


