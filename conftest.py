import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Директория для сохранения файлов
download_directory = "D:\Programs\pycharm\pycharmprogects\kulagin_tensor_test"

# Настройка параметров Chrome
chrome_options = Options()
chrome_prefs = {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", chrome_prefs)


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(10)
    return chrome_browser
