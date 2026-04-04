from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import allure


class OrderForm(BasePage):
    
    @allure.step('Заполнить "*Имя"')
    def set_name(self, name):
        self.send_keys(OrderPageLocators.ORDER_FORM_NAME, name)

    @allure.step('Заполнить "*Фамилия"')
    def set_last_name(self, last_name):
        self.send_keys(OrderPageLocators.ORDER_FORM_SURNAMENAME, last_name)

    @allure.step('Заполнить "*Адрес: куда привезти заказ"')
    def set_adds(self, adds):
        self.send_keys(OrderPageLocators.ORDER_FORM_ADDS, adds)
    
    @allure.step('Клик "*Станция метро", клик по станции "Сокольники"')
    def set_metro(self):
        self.click_element(OrderPageLocators.ORDER_FORM_METRO)
        self.click_element(OrderPageLocators.ORDER_FORM_SOKOLNIKI_METRO)

    @allure.step('Заполнить "*Телефон: на него позвонит курьер"')
    def set_telephone(self, tel):
        self.send_keys(OrderPageLocators.ORDER_FORM_MOBILE, tel)  

    @allure.step('Клик по "Далее"')
    def click_next_button(self):
        self.click_element(OrderPageLocators.ORDER_FORM_NEXT_BUTTON)

    @allure.step('Заполнить "*Когда привезти самокат"')
    def set_date(self, data):
        self.send_keys(OrderPageLocators.DETAILS_ORDER_DATE, data)

    @allure.step('Клик "*Срок аренды", клик "сутки"')
    def set_next_time(self):
        self.click_element(OrderPageLocators.DETAILS_ORDER_TIME)
        self.click_element(OrderPageLocators.DETAILS_ORDER_CHOICE_TIME_1)

    @allure.step('Клик "черный жемчуг" в блоке "Цвет самоката"')
    def choice_color_black(self):
        self.click_element(OrderPageLocators.DETAILS_ORDER_BLACK)
    
    @allure.step('Клик "серая безысходность" в блоке "Цвет самоката"')
    def choice_color_grey(self):
        self.click_element(OrderPageLocators.DETAILS_ORDER_GREY)

    @allure.step('Заполнить "Комменарий для курьера"')
    def set_comment(self, comment):
        self.send_keys(OrderPageLocators.DETAILS_ORDER_COMMENT, comment)

    @allure.step('Клик "Заказать"')
    def click_order_button(self):
        self.click_element(OrderPageLocators.DETAILS_ORDER_BUTTON)

    @allure.step('Клик "Да" для формы "Хотите оформить заказ?"')
    def click_yes_order_button(self):
        self.click_element(OrderPageLocators.DETAILS_ORDER_YES_BUTTON)
    
    @allure.step('Проверка появления блока "Заказ оформлен"')
    def is_order_successful(self): 
        return self.wait_element_is_displayed(OrderPageLocators.DETAILS_ORDER_DESIGNED)
        