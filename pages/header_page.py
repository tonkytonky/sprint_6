import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HeaderPage(BasePage):
    scooter_logo_locator = (By.XPATH, "//img[@alt = 'Scooter']")
    home_header_locator = (By.XPATH, "//div[contains(@class, 'Home_Header')]")
    yandex_logo_locator = (By.XPATH, "//img[@alt = 'Yandex']")
    yandex_header_locator = (By.XPATH, "//div[contains(@class, 'dzenHeaderContainer')]")
    order_btn_header_locator = (By.XPATH, "//div[contains(@class, 'Header')]//button[text() = 'Заказать']")

    @allure.step("Перейти на Главную страницу")
    def go_to_main_page(self):
        self.click_element(self.scooter_logo_locator)
        self.wait_element(self.home_header_locator)

    @allure.step("Перейти на Главную страницу Яндекс")
    def go_to_yandex(self):
        self.click_element(self.yandex_logo_locator)
        self.wait_element(self.yandex_header_locator)

    @allure.step("Открыть форму заказа")
    def open_order_form(self):
        self.click_element(self.order_btn_header_locator)
