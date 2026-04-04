from pages.home_page import HomePage
from data import TestUrl
import allure


class TestLogo:
    @allure.title('Проверка перехода на страницу Дзена после клика по лого Яндекса')
    def test_click_yndx_and_transfer(self, browser):
        yndx_logo = HomePage(browser) 
        yndx_logo.click_logo_yndx()
        browser.switch_to.window(browser.window_handles[-1])
        assert browser.current_url == TestUrl.YNDX_URL

    @allure.title('Проверка перехода главную страницу страницу после клика по лого Самоката')
    def test_click_samocat_and_transfer(self, browser):
        browser.get(TestUrl.ORDER_URL)
        samocat_logo = HomePage(browser) 
        samocat_logo.click_logo_samocat()
        assert browser.current_url == TestUrl.HOME_URL
