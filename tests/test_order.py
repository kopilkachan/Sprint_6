from pages.order_page import OrderForm
from pages.home_page import HomePage
from data import TestUrl, OrderData
import pytest
import allure
 

class TestOrder:
    
    @allure.title('Проверка перехода к форме заказа после клика по "Заказать" внизу страницы')
    def test_clickable_big_order_button(self, browser):
        home_order = HomePage(browser)
        home_order.click_order_big_button()
        assert browser.current_url == TestUrl.ORDER_URL
        
    @pytest.mark.parametrize("order_data", OrderData.ALL_ORDERS)
    @allure.title('Проверка создания заказа самоката')
    def test_take_order(self, browser, order_data):
        order = OrderForm(browser)
        home_order = HomePage(browser)
        home_order.click_order_in_header()
        order.set_name(order_data["name"])
        order.set_last_name(order_data["last_name"])
        order.set_adds(order_data["address"])
        order.set_metro()
        order.set_telephone(order_data["phone"])
        order.click_next_button()
        order.set_next_time()
        order.set_date(order_data["date"])
        order.choice_color_black()
        order.set_comment(order_data["comment"])
        order.click_order_button()
        order.click_yes_order_button()
        assert order.is_order_successful()
        