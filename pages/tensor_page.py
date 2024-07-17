from pages.page import Main_Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

element_selector_sila_v_ludyah = (By.XPATH, '//p[contains(@class, "tensor_ru-Index__card-title") and contains(@class, "tensor_ru-pb-16") and text()="Сила в людях"]')
button_selecotr_podrobnee = (By.LINK_TEXT, 'Подробнее')
button_selecotr_podrobnee_url = (By.XPATH, '//a[@href="/about"and text()="Подробнее"]')

class Elements(Main_Page) :
    def __init__(self, browser):
        super().__init__(browser)

    def open_url_tensor(self):
        self.open_url('https://tensor.ru/')
        sleep(3)

    def element_sila_v_ludyah(self):
        try:
            element = self.find(element_selector_sila_v_ludyah)
            assert element.is_displayed(), "Элемент присутствует, но не отображается."
        except NoSuchElementException:
            print("Элемент не найден на странице.")


    def button_podrobnee(self):
        return self.find(button_selecotr_podrobnee)

    def button_podrobnee_url_cheack(self):
        expected_url = "https://tensor.ru/about/"
        main_window = self.browser.current_window_handle
        windows = self.browser.window_handles
        for window in windows:
            if window != main_window:
                self.browser.switch_to.window(window)
                break
        assert self.browser.current_url == expected_url ,f"Ожидался URL: {expected_url}, но текущий URL: {self.browser.current_url}"
        self.browser.switch_to.window(main_window)
