from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from faker import Faker
from random import choice

class OrderPage(BasePage):
    order_button_header_locator = (By.XPATH, "//div[contains(@class, 'Header')]//button[text() = 'Заказать']")
    order_button_roadmap_locator = (By.XPATH, "//div[contains(@class, 'RoadMap')]//button[text() = 'Заказать']")

    # Форма "Для кого самокат"
    name_locator = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    surname_locator = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")
    address_locator = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")
    subway_locator = (By.XPATH, "//input[contains(@placeholder, 'метро')]")
    subway_stations_locator = (By.XPATH, "//div[@class = 'select-search__select']//li")
    phone_locator = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")
    next_btn_locator = (By.XPATH, "//button[text() = 'Далее']")

    def __init__(self, driver):
        super().__init__(driver)
        self.faker = Faker("ru_RU")

    def open_order_form_from_header(self):
        self.click_element(self.order_button_header_locator)

    def fill_order_form(self):
        self.send_keys_to_element(self.name_locator, self.faker.first_name())
        self.send_keys_to_element(self.surname_locator, self.faker.last_name())
        self.send_keys_to_element(self.address_locator, self.faker.street_address().replace("/", ""))

        self.click_element(self.subway_locator)
        subway_stations = self.driver.find_elements(*self.subway_stations_locator)
        choice(subway_stations).click()

        self.send_keys_to_element(self.phone_locator, self.faker.phone_number().replace(" ", ""))

        self.click_element(self.next_btn_locator)

        print()


