from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import config


class BasePage:
    accept_cookie_btn = (By.XPATH, "//*[contains(@class, 'App_CookieButton')]")

    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, locator: tuple[str, str]):
        element = WebDriverWait(self.driver, config.TIMEOUT).until(
            ec.visibility_of_element_located(locator))
        return element

    def click_element(self, locator: tuple[str, str]):
        element = self.wait_element(locator)
        element.click()
        return element

    def send_keys_to_element(self, locator: tuple[str, str], keys):
        element = self.wait_element(locator)
        element.send_keys(keys)

    def accept_cookies(self):
        self.click_element(self.accept_cookie_btn)
