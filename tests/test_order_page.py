from config import MAIN_PAGE_URL
from pages.header_page import HeaderPage
from pages.order_page import OrderPage


class TestOrderPage:

    def test_create_order_from_header(self, firefox_driver):
        header_page = HeaderPage(firefox_driver)
        order_page = OrderPage(firefox_driver)
        firefox_driver.get(MAIN_PAGE_URL)
        order_page.accept_cookies()

        header_page.open_order_form(locator=HeaderPage.order_btn_header_locator)
        order_page.fill_order_form_with_generated_data()
        header_page.go_to_main_page()

    def test_create_order_from_roadmap(self, firefox_driver):
        header_page = HeaderPage(firefox_driver)
        order_page = OrderPage(firefox_driver)
        firefox_driver.get(MAIN_PAGE_URL)
        order_page.accept_cookies()

        header_page.open_order_form(locator=HeaderPage.order_btn_roadmap_locator)
        order_page.fill_order_form_with_generated_data()
        header_page.go_to_yandex()
