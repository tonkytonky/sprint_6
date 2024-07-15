from datetime import datetime, timedelta
from random import choice

import allure
from faker import Faker
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderPage(BasePage):
    # Форма заказа
    name_locator = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    surname_locator = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")
    address_locator = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")
    subway_locator = (By.XPATH, "//input[contains(@placeholder, 'метро')]")
    subway_stations_locator = (By.XPATH, "//div[@class = 'select-search__select']//li")
    phone_locator = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")
    next_btn_locator = (By.XPATH, "//button[text() = 'Далее']")
    date_locator = (By.XPATH, "//input[contains(@placeholder, 'Когда')]")
    period_locator = (By.XPATH, "//div[contains(text(), 'Срок')]")
    periods_locator = (By.XPATH, "//div[@class = 'Dropdown-option']")
    black_color_locator = (By.XPATH, "//input[@id = 'black']")
    grey_color_locator = (By.XPATH, "//input[@id = 'grey']")
    color_locators = [black_color_locator, grey_color_locator]
    order_btn_locator = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text() = 'Заказать']")
    yes_btn_locator = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text() = 'Да']")
    status_btn_locator = (By.XPATH, "//button[text() = 'Посмотреть статус']")

    def __init__(self, driver):
        super().__init__(driver)
        self.faker = Faker("ru_RU")

    @allure.step('Заполнить форму заказа: Раздел "Для кого самокат"')
    def fill_order_form_section_scooter_with_generated_data(self):
        self.send_keys_to_element(self.name_locator, self.faker.first_name())
        self.send_keys_to_element(self.surname_locator, self.faker.last_name())

        street_address = self.faker.street_address().replace("/", "")
        self.send_keys_to_element(self.address_locator, street_address)

        self.click_element(self.subway_locator)
        subway_stations = self.driver.find_elements(*self.subway_stations_locator)
        choice(subway_stations).click()

        phone_number = self.faker.phone_number()
        for forbidden_char in (" ", "-", "(", ")"):
            phone_number = phone_number.replace(forbidden_char, "")
        self.send_keys_to_element(self.phone_locator, phone_number)

        self.click_element(self.next_btn_locator)

    @allure.step('Заполнить форму заказа: Раздел "Про аренду"')
    def fill_order_form_section_rent_with_generated_data(self):
        date = self.faker.date_between(datetime.now(), timedelta(days=14)).strftime("%d.%m.%Y")
        self.send_keys_to_element(self.date_locator, date)
        self.send_keys_to_element(self.date_locator, Keys.ESCAPE)

        self.click_element(self.period_locator)
        periods = self.driver.find_elements(*self.periods_locator)
        choice(periods).click()

        color_locator = choice(self.color_locators)
        self.click_element(color_locator)

        self.click_element(self.order_btn_locator)
        self.click_element(self.yes_btn_locator)
        self.click_element(self.status_btn_locator)
