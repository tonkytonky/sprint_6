from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HeaderPage(BasePage):
    scooter_logo_locator = (By.XPATH, "//img[@alt = 'Scooter']")
    home_header_locator = (By.XPATH, "//div[contains(@class, 'Home_Header')]")
    yandex_logo_locator = (By.XPATH, "//img[@alt = 'Yandex']")
    yandex_header_locator = (By.XPATH, "//div[contains(@class, 'dzenHeaderContainer')]")
    order_btn_header_locator = (By.XPATH, "//div[contains(@class, 'Header')]//button[text() = 'Заказать']")
    order_btn_roadmap_locator = (By.XPATH, "//div[contains(@class, 'RoadMap')]//button[text() = 'Заказать']")

    def go_to_main_page(self):
        self.click_element(self.scooter_logo_locator)
        self.wait_element(self.home_header_locator)

    def go_to_yandex(self):
        self.click_element(self.yandex_logo_locator)
        self.wait_element(self.yandex_header_locator)

    def open_order_form(self, locator):
        self.click_element(locator)
