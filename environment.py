from selenium import webdriver

def before_all(context):
    browser = webdriver.Chrome(r'.\\lib\\chromedriver.exe')
    browser.implicitly_wait(5)
    browser.set_window_size(1920, 1080)
    context.browser = browser
    context.screenshot_buffer = {}


def after_all(context):
    context.browser.quit()
