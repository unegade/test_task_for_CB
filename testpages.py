from selenium import webdriver
from pages.google_page import GoogleStartPage
from pages.cbr_page import CBRPage, CBRReceptionPage, CBRReceptionMessagePage, CBRAboutWarningPage

browser = webdriver.Chrome(r'.//chromedriver.exe')
browser.implicitly_wait(5)
browser.set_window_size(1920,1080)
try:
    googlePage = GoogleStartPage(browser, 'http://google.ru')
    googlePage.check_search_field()
    googlePage.insert_text_in_search_field('Центральный банк РФ')
    googlePage.click_search_button()
    googlePage.go_to_result_link_by_partial_link_text('cbr.ru')
    cbrPage = CBRPage(googlePage.getBrowser())
    # cbrPage = CBRPage(browser,'https://www.cbr.ru/analytics/fin_stab/')
    cbrPage.reception_click()
    cbrPage = CBRReceptionPage(cbrPage.getBrowser())
    cbrPage.write_thanks_click()
    cbrPage = CBRReceptionMessagePage(cbrPage.getBrowser())
    cbrPage.enter_thanks_message('случайный текст')
    cbrPage.agreement_flag_click()
    screen = cbrPage.getScreenshot()
    cbrPage.site_map_button_click()
    cbrPage.site_map_about_click()
    cbrPage.site_map_about_warning_click()
    cbrPage = CBRAboutWarningPage(cbrPage.getBrowser())
    ru_text = cbrPage.getWarningText()
    cbrPage.en_language_click()
    en_text = cbrPage.getWarningText()
    print(len(set(ru_text) & set(en_text)) == 0)
finally:
    browser.quit()