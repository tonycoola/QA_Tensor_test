from pages.sbis_page import Buttons
from pages.tensor_page import Elements
from pages.tensor_about_page import Elements_Tensor_About


def test_buttons_sbis_section_1(browser):
    #инициализируем сессию с классом и браузером
    browser_section = Buttons(browser)

    # 1 Переходим по ссылке http/sbis/clients
    browser_section.open_url_sbis_clients()

    # 2  Проверяем наличие лого Тензор и кликаем на него
    assert browser_section.button_tensor_logo().is_displayed()
    browser_section.button_tensor_logo().click()

    # 3 Проверяем что перешли на /tensor
    browser_section.button_tensor_logo_url_check()
    print("Тест /sbis/clients секции 1 пройден")

def test_elements_tensor_section_1(browser):
    browser_section_2 = Elements(browser)

    # 3.1 Переходим на /tensor
    browser_section_2.open_url_tensor()

    # 4 Проверяем наличие элемента Сила в Людях
    browser_section_2.element_sila_v_ludyah()

    # 5 Проверяем наличие Кнопки "Подробнее"
    assert browser_section_2.button_podrobnee().is_displayed()

    # Кликаем на кнопку "Подробнее"
    browser_section_2.button_podrobnee().click()

    # 5.1 Проверяем,что перешли на tensor/about
    browser_section_2.button_podrobnee_url_cheack()
    print("Тест /tensor секции 1 пройден")

def test_buttons_tensor_about_section_1(browser):
    browser_section_4 = Elements_Tensor_About(browser)

    # Переходим на tensor/about
    browser_section_4.open_url_tensor_about()

    #Проверяем наличие раздела "Работаем"
    assert browser_section_4.element_rabotaem().is_displayed()

    #Проверяем наличие картинок и размеры картинок
    browser_section_4.check_images_same_size()
    print("Тест tensor/about секции 1 пройден")
