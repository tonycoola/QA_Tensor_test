from time import sleep
from pages.sbis_page import Buttons

def test_buttons_section_2(browser):
    # инициализируем сессию с классом и браузером
    browser_section = Buttons(browser)

    # 1 Переходим по ссылке http/sbis/clients первого теста
    browser_section.open_url_sbis_clients()

    # 2 Проверяем что подставился регион Ярослвской обл
    assert browser_section.button_yar_region_cheack().is_displayed()

    # Появился список партернов Ярославской обл
    assert browser_section.element_yar_partners_region_cheack().is_displayed()

    #Клик на кнопку Ярославской обл.
    browser_section.button_yar_region_cheack().click()
    #Ожидание 3 сек
    sleep(3)

    # 3 Изменяем кликом регион на Камчатский
    browser_section.button_kamchatski_region_click()
    sleep(3)

    # 4 Проверяем появление камчатского региона на кнопке
    assert browser_section.button_kamchatski_region_cheack().is_displayed()

    # Проверяем появление камчатского региона в списке партнеров
    assert browser_section.element_kamchatski_partners_region_cheack().is_displayed()

    # Проверить появление kamchatskij в url
    browser_section.kamchatski_url_check()

    # Проверить появление в title "Камчатский"
    browser_section.check_title_contains()

    print("Тест /sbis/clients секции 2 пройден")