"""
Cоздаем абстрактный класс, где есть метод инициализации этого класса и методы для
упрощения написания поиска элементов
"""


class Main_Page:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    def open_url(self, url):
        self.browser.get(url)