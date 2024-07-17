from time import sleep
from pages.sbis_page_main import DownloadPage

def test_buttons_section_3(browser):
    # инициализируем сессию с классом и браузером
    browser_section_3 = DownloadPage(browser)

    # 1 Переходим по ссылке http/sbis/
    browser_section_3.open_url_sbis()

    #2 Клик на  локальные версии
    browser_section_3.click_local_versions()

    #3 Скачать версию в папку @\kulagin_tensor_test
    browser_section_3.save_windows_web_version()

    #4 Проверка,что файл скачался
    browser_section_3.saving_windows_web_version_check()

    #5 Проврека размера файла
    browser_section_3.windows_web_version_wieght_check()