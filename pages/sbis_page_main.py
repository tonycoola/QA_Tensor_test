from pages.page import Main_Page
from selenium.webdriver.common.by import By
from time import sleep
from conftest import download_directory
import os
import re

local_versions_selector = (By.LINK_TEXT, 'Скачать локальные версии')
save_windows_web_version_selector = (By.XPATH, '//a[contains(text(), "Скачать") and contains(text(), "Exe")]')
save_windows_web_version_selector_on_PC = (By.XPATH,'//div [@class="sbis_ru-DownloadNew-loadLink"]')
#save_windows_web_version_selector = (By.XPATH, '//a[@href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')
file_name = "sbisplugin-setup-web.exe"

class DownloadPage(Main_Page) :

    def __init__(self, browser):
        super().__init__(browser)

    def click_local_versions(self):
        return self.find(local_versions_selector).click()
        sleep(3)

    def open_url_sbis(self):
        self.open_url('https://sbis.ru/')
        sleep(3)

    def save_windows_web_version(self):
        self.find(save_windows_web_version_selector_on_PC).click()
        #Грубое ожидание скачивание файла
        sleep(10)

    # Проверка наличия файла в директории
    def saving_windows_web_version_check(self):
        # Путь файла
        file_path = os.path.join(download_directory, file_name)
        # Проверка, есть ли файл в пути?
        assert os.path.isfile(file_path), f"{file_name} не найден."
        print(f"{file_name} успешно скачан.")

    #Проверка веса файла
    def windows_web_version_wieght_check(self):
        # expected_file_size_mb = 11.05
        #expected_file_size_text ищем текст 11.05
        expected_file_size_text = self.find(save_windows_web_version_selector).get_attribute('textContent')

        # Извлечение числового значения из текста
        match = re.search(r'(\d+\.\d+) МБ', expected_file_size_text)
        # Извлекаем из группы 1 число в мб
        expected_file_size_mb = float(match.group(1))

        # Проверка размера файла
        file_path = os.path.join(download_directory, file_name)
        #Переводим в МБ
        actual_file_size_mb = os.path.getsize(file_path)/ (1024 * 1024)
        assert abs(actual_file_size_mb - expected_file_size_mb) < 0.01, f"Размер файла не соответствует ожидаемому. " \
                                                                        f"Ожидалось: {expected_file_size_mb}, " \
                                                                        f"Получено: {actual_file_size_mb}"

        print("Файл успешно скачан и его размер соответствует ожидаемому.")