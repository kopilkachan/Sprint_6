from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.home_page_locators import HomePageLocators
from selenium.common.exceptions import TimeoutException


class HomePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def click_question_and_verify_answer(self, question_locator):
       element = self.wait.until(EC.presence_of_element_located(question_locator))
       self.driver.execute_script("arguments[0].scrollIntoView();", element) 
       self.wait.until(EC.element_to_be_clickable(question_locator)).click()

    def answer_is_displayed(self, answer_locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(answer_locator)).is_displayed()
        except TimeoutException:
            return False
       
    def click_logo_samocat(self):
        self.wait.until(EC.element_to_be_clickable(HomePageLocators.HEADER_LOGO_SCOOTER)).click()

    def click_logo_yndx(self):
        self.wait.until(EC.element_to_be_clickable(HomePageLocators.HEADER_LOGO_YNDX)).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait.until(EC.url_contains("https://dzen.ru/?yredirect=true"))
        