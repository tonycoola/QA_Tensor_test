from time import sleep
from pages.sbis_page import Buttons

def test_buttons_section_2(browser):
    # инициализируем сессию с классом и браузером
    Buttons(browser)

    # 1 Переходим по ссылке http/sbis/clients первого теста
    Buttons(browser).open_url_sbis_clients()

    # 2 Проверяем что подставился регион Ярослвской обл
    assert Buttons(browser).button_yar_region_cheack().is_displayed()

    # Появился список партернов Ярославской обл
    assert Buttons(browser).element_yar_partners_region_cheack().is_displayed()

    #Клик на кнопку Ярославской обл.
    Buttons(browser).button_yar_region_cheack().click()
    #Ожидание 3 сек
    sleep(3)

    # 3 Изменяем кликом регион на Камчатский
    Buttons(browser).button_kamchatski_region_click()
    sleep(3)

    # 4 Проверяем появление камчатского региона на кнопке
    assert Buttons(browser).button_kamchatski_region_cheack().is_displayed()

    # Проверяем появление камчатского региона в списке партнеров
    assert Buttons(browser).element_kamchatski_partners_region_cheack().is_displayed()

    # Проверить появление kamchatskij в url
    Buttons(browser).kamchatski_url_check()

    # Проверить появление в title "Камчатский"
    Buttons(browser).check_title_contains()

    print("Тест /sbis/clients секции 2 пройден")