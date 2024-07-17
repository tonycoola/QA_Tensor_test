from time import sleep
from pages.sbis_page_main import DownloadPage

def test_buttons_section_3 (browser):
    # инициализируем сессию с классом и браузером
    DownloadPage(browser)

    # 1 Переходим по ссылке http/sbis/
    DownloadPage(browser).open_url_sbis()

    #2 Клик на  локальные версии
    DownloadPage(browser).click_local_versions()

    #3 Скачать версию в папку @\kulagin_tensor_test
    DownloadPage(browser).save_windows_web_version()

    #4 Проверка,что файл скачался
    DownloadPage(browser).saving_windows_web_version_check()

    #5 Проврека размера файла
    DownloadPage(browser).windows_web_version_wieght_check()