from selenium.webdriver.support import expected_conditions as EC
from locators.home_page_locators import HomePageLocators
from data import TestUrl
from pages.base_page import BasePage
import allure


class HomePage(BasePage):
    @allure.step('Клик по вопросу из Faq')
    def click_question(self, question_locator):
       self.scroll_to_element(question_locator)
       self.click_element(question_locator)

    @allure.step('Проверка открытия соответствующего ответа')
    def answer_is_displayed(self, answer_locator):
        return self.wait_element_is_displayed(answer_locator)
       
    @allure.step('Клик по лого "Самоката"')
    def click_logo_samocat(self):
        self.click_element(HomePageLocators.HEADER_LOGO_SCOOTER)

    @allure.step('Клик по лого "Яндекса"')
    def click_logo_yndx(self):
        self.click_element(HomePageLocators.HEADER_LOGO_YNDX)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait.until(EC.url_contains(TestUrl.YNDX_URL))

    @allure.step('Клик по "Заказать" на хедере')
    def click_order_in_header(self):
        self.click_element(HomePageLocators.HEADER_ORDER_BUTTON)
        
    @allure.step('Клик по "Заказать" внизу страницы')
    def click_order_big_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_element(HomePageLocators.BIG_ORDER_BUTTON)
        