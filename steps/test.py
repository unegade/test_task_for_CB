from behave import *
from lib.pages.google_page import GoogleStartPage
from lib.pages.cbr_page import *


@when('Открыли сайт "{url}"')
def step(context, url: str):
    context.page = GoogleStartPage(context.browser, url)


@then(u'Появится поле поиск')
def step(context):
    context.page.check_search_field()


@when(u'Ввели в поле поиска "{text}"')
def step(context, text: str):
    context.page = GoogleStartPage(context.browser)
    context.page.insert_text_in_search_field(text)


@when(u'Нажали на кнопку поиск в google')
def step(context):
    context.page.click_search_button()


@then(u'Появится ссылка на {text}')
def step(context, text: str):
    context.page.check_result_link_by_partial_link_text(text)


@when(u'Перешли на по первой из ссылок содержащих адресс "{text}"')
def step_impl(context, text: str):
    context.page = GoogleStartPage(context.browser)
    context.page.go_to_result_link_by_partial_link_text(text)
    # raise NotImplementedError(u'STEP: When Перешли на по первой из ссылок')


@then(u'Откроется сайт https://www.cbr.ru')
def step_impl(context):
    context.page = CBRPage(context.browser)
    assert context.page.check_is_cbr_page()

@when(u'Нажали на ссылку Интернет-приемная')
def step_impl(context):
    context.page = CBRPage(context.browser)
    context.page.reception_click()


@when(u'Открыли раздел Написать благодарность')
def step_impl(context):
    context.page = CBRReceptionPage(context.browser)
    context.page.write_thanks_click()


@when(u'В поле Ваша благодарность ввели значение “{text}”')
def step_impl(context, text: str):
    context.page = CBRReceptionMessagePage(context.browser)
    context.page.enter_thanks_message(text)


@when(u'Поставили галочку “Я согласен”')
def step_impl(context):
    context.page.agreement_flag_click()


@then(u'Сделать скриншот')
def step_impl(context):
    context.screenshot_buffer[context.browser.title] = context.page.getScreenshot()


@when(u'Нажали на кнопку меню ("Три полоски")')
def step_impl(context):
    context.page = CBRPage(context.browser)
    context.page.site_map_button_click()


@when(u'Нажали на раздел О сайте')
def step_impl(context):
    context.page.site_map_about_click()


@when(u'Нажали на ссылку предупреждение')
def step_impl(context):
    context.page.site_map_about_warning_click()


@when(u'Запомнили текст предупреждения на русском')
def step_impl(context):
    context.page = CBRAboutWarningPage(context.browser)
    context.ru_text = context.page.getWarningText()


@when(u'Сменили язык страницы на Английский')
def step_impl(context):
    context.page.en_language_click()


@then(u'Текст на английском должен отличаться от текста на русском')
def step_impl(context):
    en_text = context.page.getWarningText()
    assert len(context.ru_text & en_text) == 0

