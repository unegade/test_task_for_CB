from selenium import webdriver
from selenium.webdriver import Remote

class BasePage():
    def __init__(self, browser:Remote, url=None):
        self.browser = browser
        if url:
            self.url = url
            self.browser.get(self.url)
        else:
            # Если открывается новая вкладка то фокусируем ее
            # В будующем найти решение данного костыля
            self.browser.switch_to_window(self.browser.window_handles[-1])


    def getBrowser(self) -> Remote:
        """Возвращает экзепляр текущего браузера"""
        return self.browser
        

    def getScreenshot(self) -> bytes:
        return self.browser.get_screenshot_as_png()
