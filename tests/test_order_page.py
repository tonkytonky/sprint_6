import allure

from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title("Создать заказ по кнопке в Заголовке Главной страницы")
    def test_create_order_from_header(self, firefox_driver):
        main_page = MainPage(firefox_driver)
        header_page = HeaderPage(firefox_driver)
        order_page = OrderPage(firefox_driver)
        main_page.open_page()
        main_page.accept_cookies()

        header_page.open_order_form()
        order_page.fill_order_form_section_scooter_with_generated_data()
        order_page.fill_order_form_section_rent_with_generated_data()
        header_page.go_to_main_page()

    @allure.title("Создать заказ по кнопке на Главной странице")
    def test_create_order_from_roadmap(self, firefox_driver):
        main_page = MainPage(firefox_driver)
        header_page = HeaderPage(firefox_driver)
        order_page = OrderPage(firefox_driver)
        main_page.open_page()
        main_page.accept_cookies()

        main_page.open_order_form()
        order_page.fill_order_form_section_scooter_with_generated_data()
        order_page.fill_order_form_section_rent_with_generated_data()
        header_page.go_to_yandex()
