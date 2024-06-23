from pages.questions_page import QuestionsPage
from tests.base_test import BaseTest


class TestQuestionsPage(BaseTest):

    @classmethod
    def setup_class(cls):
        cls.create_driver()
        cls.questions_page = QuestionsPage(cls.driver)

    def test_questions_answers_mapping(self):
        self.driver.get(self.questions_page.url)
        self.questions_page.accept_cookies()

        self.questions_page.check_questions()
