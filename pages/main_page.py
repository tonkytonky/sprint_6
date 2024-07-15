import allure
from selenium.webdriver.common.by import By

from config import MAIN_PAGE_URL
from pages.base_page import BasePage


class MainPage(BasePage):
    question_locator_template = (By.ID, "accordion__heading-{}")
    questions_locator = (By.CLASS_NAME, "accordion__heading")
    answer_locator_template = (By.ID, "accordion__panel-{}")
    order_btn_roadmap_locator = (By.XPATH, "//div[contains(@class, 'RoadMap')]//button[text() = 'Заказать']")

    @allure.step("Открыть Главную страницу")
    def open_page(self):
        self.driver.get(MAIN_PAGE_URL)

    @staticmethod
    def _format_template(template: tuple, index):
        return template[0], template[1].format(index)

    def _build_question_locator(self, index):
        question_locator = self._format_template(self.question_locator_template, index)
        return question_locator

    def _build_answer_locator(self, index):
        answer_locator = self._format_template(self.answer_locator_template, index)
        return answer_locator

    @allure.step("Извлечь вопросы и ответы с сайта")
    def fetch_question_answer_mapping_actual(self):
        self.wait_element(self._build_question_locator(index=0))

        question_max_index = len(self.driver.find_elements(*self.questions_locator)) - 1
        question_answer_mapping_actual = {}
        for accordion_number in range(question_max_index, -1, -1):
            question_locator = self._build_question_locator(index=accordion_number)
            answer_locator = self._build_answer_locator(index=accordion_number)

            question = self.click_element(question_locator)
            answer = self.wait_element(answer_locator)

            question_answer_mapping_actual[question.text] = answer.text

        return question_answer_mapping_actual

    @allure.step("Открыть форму заказа")
    def open_order_form(self):
        self.click_element(self.order_btn_roadmap_locator)
