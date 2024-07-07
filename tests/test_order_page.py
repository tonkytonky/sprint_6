from selenium.webdriver.support.ui import Select

from config import MAIN_PAGE_URL
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    def test_order_page(self, driver):
        order_page = OrderPage(driver)
        driver.get(MAIN_PAGE_URL)
        order_page.accept_cookies()

        order_page.open_order_form_from_header()
        order_page.fill_order_form()


