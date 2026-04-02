from pages.order_page import OrderForm
from data import TestUrl, OrderData
import pytest
 

class TestOrder:
    
    def test_clickable_big_order_button(self, browser):
        big_button = OrderForm(browser)
        big_button.click_order_big_button()
        assert browser.current_url == TestUrl.ORDER_URL
        
    @pytest.mark.parametrize("order_data", OrderData.ALL_ORDERS)
    def test_take_order(self, browser, order_data):
        order = OrderForm(browser)
        order.click_order_in_header()
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
        