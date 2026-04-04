from selenium.webdriver.common.by import By


class OrderPageLocators:

    ORDER_FORM_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
    ORDER_FORM_SURNAMENAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ORDER_FORM_ADDS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    ORDER_FORM_METRO = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    ORDER_FORM_SOKOLNIKI_METRO = (By.XPATH, ".//li[@data-value='4']")
    ORDER_FORM_MOBILE = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    ORDER_FORM_NEXT_BUTTON = (By.XPATH, ".//button[text() = 'Далее']")

    DETAILS_ORDER_DATE = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    DETAILS_ORDER_TIME = (By.XPATH, ".//div[text() = '* Срок аренды']")
    DETAILS_ORDER_CHOICE_TIME_1 = (By.XPATH, ".//div[text() = 'сутки']")
    DETAILS_ORDER_BLACK = (By.XPATH, ".//label[@for='black']")
    DETAILS_ORDER_GREY = (By.XPATH, ".//label[@for='grey']")
    DETAILS_ORDER_COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    DETAILS_ORDER_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    DETAILS_ORDER_YES_BUTTON = (By.XPATH, ".//button[text() = 'Да']")
    DETAILS_ORDER_DESIGNED = (By.XPATH, ".//div[text() = 'Заказ оформлен']")
    