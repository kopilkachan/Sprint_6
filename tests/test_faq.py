import pytest
from pages.home_page import HomePage
from data import FAQ_DATA
import allure


class TestFaq:
    @pytest.mark.parametrize("question_locator, answer_locator", FAQ_DATA.QA)
    @allure.title('Проверка соответствия вопроса и ответа в блоке FAQ на главной странице')
    def test_faq_check_correlated(self, browser, question_locator, answer_locator):
        faq = HomePage(browser)
        faq.click_question(question_locator) 
        assert faq.answer_is_displayed(answer_locator)
