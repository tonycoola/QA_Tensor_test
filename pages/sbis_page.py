from pages.page import Main_Page
from selenium.webdriver.common.by import By
from time import sleep

element_kamchatski_partners_region_selector = (By.XPATH, '// div[ @ id = "city-id-2" and text() = "Петропавловск-Камчатский"]')
kamchatski_region_selector = (By.XPATH,'//span[contains(@class, "sbis_ru-Region-Chooser__text") and contains(@class, "sbis_ru-link") and text()="Камчатский край"]')
button_kamchatski_region_selector = (By.CSS_SELECTOR,'span[title="Камчатский край"]')
element_yar_partners_region_selector = (By.XPATH,'// div[ @ id = "city-id-2" and text() = "Ярославль"]')
yar_region_selector = (By.XPATH,'//span[contains(@class, "sbis_ru-Region-Chooser__text") and contains(@class, "sbis_ru-link") and text()="Ярославская обл."]')
button_selection_tensor_logo = (By.CLASS_NAME,'sbisru-Contacts__logo-tensor')


class Buttons(Main_Page) :
    def __init__(self, browser):
        super().__init__(browser)

    def open_url_sbis_clients(self):
        self.open_url('https://sbis.ru/contacts/76-yaroslavskaya-oblast?tab=clients')
        sleep(3)

    def button_tensor_logo(self):
        return self.find(button_selection_tensor_logo)

    def button_yar_region_cheack(self):
        return self.find(yar_region_selector)

    def element_yar_partners_region_cheack(self):
        return self.find(element_yar_partners_region_selector)

    def button_kamchatski_region_click(self):
        return self.find(button_kamchatski_region_selector).click()

    def button_kamchatski_region_cheack(self):
        return self.find(kamchatski_region_selector)

    def element_kamchatski_partners_region_cheack(self):
        return self.find(element_kamchatski_partners_region_selector)

    def button_tensor_logo_url_check(self):
        expected_url = "https://tensor.ru/"
        main_window = self.browser.current_window_handle
        windows = self.browser.window_handles
        for window in windows:
            if window != main_window:
                self.browser.switch_to.window(window)
                break
        assert self.browser.current_url == expected_url, f"Ожидался URL: {expected_url}, но текущий URL: {self.browser.current_url}"
        self.browser.switch_to.window(main_window)

    def kamchatski_url_check(self):
        assert "kamchatskij-kraj" in self.browser.current_url,f"Ожидался в URL: kamchatskij-kraj, но текущий URL: {self.browser.current_url}"

    def check_title_contains(self):
        try:
            title = self.browser.title
            assert "Камчатский" in title, f"Заголовок '{title}' не содержит Камчатский"
        except AssertionError as e:
            print(e)
