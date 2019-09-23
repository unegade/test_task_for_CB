from selenium import webdriver
from lib.email_sender import EmailSender

def before_all(context):
    browser = webdriver.Chrome(r'.\\lib\\chromedriver.exe')
    browser.implicitly_wait(5)
    browser.set_window_size(1920, 1080)
    context.browser = browser
    context.screenshot_buffer = {}


def after_all(context):
    context.browser.quit()
    mailSender = EmailSender('cbrsender@yandex.ru', 'cbrsender0')
    mailSender.send_mail('unegade@gmail.com', 'Behave test result', 'Тест закончился', context.screenshot_buffer)

