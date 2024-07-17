import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# Директория для сохранения файлов
current_directory = os.path.dirname(os.path.abspath(__file__))  # Текущая рабочая директория скрипта
download_directory = os.path.join(current_directory, "section_3_download_check")

# Настройка параметров Chrome. Используем новую директорию для скачивания.
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
