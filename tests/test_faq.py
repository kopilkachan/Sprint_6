import pytest
from pages.home_page import HomePage
from data import FAQ_DATA


class TestFaq:
 
    @pytest.mark.parametrize("question_locator, answer_locator", FAQ_DATA.QA)
    def test_faq_check_correlated(self, browser, question_locator, answer_locator):
        faq = HomePage(browser)
        faq.click_question_and_verify_answer(question_locator) 
        assert faq.answer_is_displayed(answer_locator)
