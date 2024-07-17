from conftest import browser
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
# создаем абстрактный класс, где есть метод инициализации этого класса и метод для упрощения написания поиска элементов
class Main_Page:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    def open_url(self, url):
        self.browser.get(url)