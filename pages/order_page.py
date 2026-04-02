from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from selenium.common.exceptions import TimeoutException
from locators.home_page_locators import HomePageLocators


class OrderForm:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def click_order_in_header(self):
        self.wait.until(EC.element_to_be_clickable(HomePageLocators.HEADER_ORDER_BUTTON)).click()

    def click_order_big_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait.until(EC.element_to_be_clickable(HomePageLocators.BIG_ORDER_BUTTON)).click()
    
    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.ORDER_FORM_NAME).send_keys(name)

    def set_last_name(self, last_name):
        self.driver.find_element(*OrderPageLocators.ORDER_FORM_SURNAMENAME).send_keys(last_name)

    def set_adds(self, adds):
        self.driver.find_element(*OrderPageLocators.ORDER_FORM_ADDS).send_keys(adds)
    
    def set_metro(self):
        self.driver.find_element(*OrderPageLocators.ORDER_FORM_METRO).click()
        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ORDER_FORM_SOKOLNIKI_METRO))
        self.driver.find_element(*OrderPageLocators.ORDER_FORM_SOKOLNIKI_METRO).click()

    def set_telephone(self, tel):
        self.driver.find_element(*OrderPageLocators.ORDER_FORM_MOBILE).send_keys(tel)   

    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.ORDER_FORM_NEXT_BUTTON).click()

    def set_date(self, data):
        self.driver.find_element(*OrderPageLocators.DETAILS_ORDER_DATE).send_keys(data)

    def set_next_time(self):
        self.driver.find_element(*OrderPageLocators.DETAILS_ORDER_TIME).click()
        self.driver.find_element(*OrderPageLocators.DETAILS_ORDER_CHOICE_TIME_1).click()

    def choice_color_black(self):
        self.driver.find_element(*OrderPageLocators.DETAILS_ORDER_BLACK).click()
    
    def choice_color_grey(self):
        self.driver.find_element(*OrderPageLocators.DETAILS_ORDER_GREY).click()

    def set_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.DETAILS_ORDER_COMMENT).send_keys(comment) 

    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.DETAILS_ORDER_BUTTON).click()

    def click_yes_order_button(self):
        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.DETAILS_ORDER_YES_BUTTON)).click()
    
    def is_order_successful(self): 
        try:
            return self.wait.until(EC.visibility_of_element_located(OrderPageLocators.DETAILS_ORDER_DESIGNED)).is_displayed()
        except TimeoutException:
            return False
        