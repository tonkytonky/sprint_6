from time import sleep

from assertpy import assert_that
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class QuestionsPage(BasePage):

    question = (By.CLASS_NAME, "accordion__button")
    answer = (By.XPATH, "//div[@class = 'accordion__panel']/p")
    question_answer_mapping = {
        "Сколько это стоит? И как оплатить?": "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        "Хочу сразу несколько самокатов! Так можно?": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "Как рассчитывается время аренды?": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "Можно ли заказать самокат прямо на сегодня?": "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "Можно ли продлить заказ или вернуть самокат раньше?": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "Вы привозите зарядку вместе с самокатом?": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        "Можно ли отменить заказ?": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "Я жизу за МКАДом, привезёте?": "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
    }

    def open_question(self):
        self.click_element(self.question)
        sleep(10)

    def check_questions(self):
        self.wait_element(self.question)
        questions = self.driver.find_elements(*self.question)
        answers = self.driver.find_elements(*self.answer)

        question_answer_mapping_actual = {}
        for question, actual_answer in zip(questions, answers):
            question_answer_mapping_actual[question.text] = actual_answer.text

        description = "Ответы на вопросы не совпадают"
        assert_that(self.question_answer_mapping).described_as(description).is_equal_to(question_answer_mapping_actual)
