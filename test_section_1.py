from pages.sbis_page import Buttons
from pages.tensor_page import Elements
from pages.tensor_about_page import Elements_Tensor_About


def test_buttons_sbis_section_1 (browser):
    #инициализируем сессию с классом и браузером
    Buttons(browser)

    # 1 Переходим по ссылке http/sbis/clients
    Buttons(browser).open_url_sbis_clients()

    # 2  Проверяем наличие лого Тензор и кликаем на него
    assert Buttons(browser).button_tensor_logo().is_displayed()
    Buttons(browser).button_tensor_logo().click()

    # 3 Проверяем что перешли на /tensor
    Buttons(browser).button_tensor_logo_url_check()
    print("Тест /sbis/clients секции 1 пройден")

def test_elements_tensor_section_1 (browser):
    # 3.1 Переходим на /tensor
    Elements(browser).open_url_tensor()
    # 4 Проверяем наличие элемента Сила в Людях
    Elements(browser).element_sila_v_ludyah()

    # 5 Проверяем наличие Кнопки "Подробнее"
    assert Elements(browser).button_podrobnee().is_displayed()
    # Кликаем на кнопку "Подробнее"
    Elements(browser).button_podrobnee().click()

    # 5.1 Проверяем,что перешли на tensor/about
    Elements(browser).button_podrobnee_url_cheack()
    print("Тест /tensor секции 1 пройден")

def test_buttons_tensor_about_section_1(browser):

    # Переходим на tensor/about
    Elements_Tensor_About(browser).open_url_tensor_about()

    #Проверяем наличие раздела "Работаем"
    assert Elements_Tensor_About(browser).element_rabotaem().is_displayed()

    #Проверяем наличие картинок и размеры картинок
    Elements_Tensor_About(browser).check_images_same_size()
    print("Тест tensor/about секции 1 пройден")
