from pages.page import Main_Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

element_rabotaem_selector = (By.XPATH,'//h2[contains(@class, "tensor_ru-header-h2") '
                                      'and contains(@class, "tensor_ru-About__block-title") and text()="Работаем"]')

class Elements_Tensor_About(Main_Page):
    def __init__(self, browser):
        super().__init__(browser)

    def open_url_tensor_about(self):
        self.browser.get('https://tensor.ru/about/')

    def element_rabotaem(self):
        return self.find(element_rabotaem_selector)

    def check_images_same_size(self):
        """
        Метод проверяет,что размеры картинок одинковы.
        """
        # Список селекторов для всех картинок
        picture_selectors = [
            (By.XPATH, '//img[@alt="Продвигаем сервисы"]'),
            (By.XPATH, '//img[@alt="Разрабатываем систему СБИС"]'),
            (By.XPATH, '//img[@alt="Создаем инфраструктуру"]'),
            (By.XPATH, '//img[@alt="Сопровождаем клиентов"]')
        ]

        # Список для хранения размеров картинок
        sizes = []

        try:
            for selector in picture_selectors:
                img = self.find(selector)
                width = img.get_attribute("width")
                height = img.get_attribute("height")
                sizes.append((width, height))

            # Проверка, что все размеры одинаковы
            first_size = sizes[0]
            for size in sizes:
                assert size == first_size, f"Одна картинка имеет размер {size}, но ожидалось {first_size}"

            print("Все картинки одного размера:", first_size)

        except NoSuchElementException:
            print("Одна из картинок не найдена на странице.")
        except AssertionError as e:
            print(e)
