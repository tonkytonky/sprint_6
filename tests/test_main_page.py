from assertpy import assert_that

from config import MAIN_PAGE_URL
from data import QUESTION_ANSWER_MAPPING
from pages.main_page import MainPage


class TestMainPage:

    def test_questions_answers_mapping(self, firefox_driver):
        main_page = MainPage(firefox_driver)
        firefox_driver.get(MAIN_PAGE_URL)
        main_page.accept_cookies()

        question_answer_mapping_actual = main_page.fetch_question_answer_mapping_actual()
        description = "Ответы на вопросы не совпадают"
        assert_that(QUESTION_ANSWER_MAPPING, description).is_equal_to(question_answer_mapping_actual)
