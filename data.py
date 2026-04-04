from locators.home_page_locators import HomePageLocators

class TestUrl:
    
    HOME_URL = 'https://qa-scooter.praktikum-services.ru/'
    YNDX_URL = 'https://dzen.ru/?yredirect=true'
    ORDER_URL = 'https://qa-scooter.praktikum-services.ru/order'

class FAQ_DATA:
    
    QA = [
    (HomePageLocators.Q_PRICE, HomePageLocators.A_PRICE),
    (HomePageLocators.Q_MANY_CSOOTERS, HomePageLocators.A_MANY_CSOOTERS),
    (HomePageLocators.Q_TIME, HomePageLocators.A_TIME),
    (HomePageLocators.Q_ORDER_TODAY, HomePageLocators.A_ORDER_TODAY),
    (HomePageLocators.Q_EXTEND_SHORTEN, HomePageLocators.A_EXTEND_SHORTEN),
    (HomePageLocators.Q_CHARGE, HomePageLocators.A_CHARGE),
    (HomePageLocators.Q_CANCEL, HomePageLocators.A_CANCEL),
    (HomePageLocators.Q_MKAD, HomePageLocators.A_MKAD),
    ]

class OrderData:
    
    ORDER_1 = {
        "name": "Автотест",
        "last_name": "Автотестов",
        "address": "ул. Тестовая, 1",
        "phone": "+7000000000",
        "date": "01.04.2026",
        "comment": "Тестовый комментарий"
    }

    ORDER_2 = {
        "name": "Мехроб",
        "last_name": "Азизов",
        "address": "ул. бессоница, 24",
        "phone": "+7111111111",
        "date": "22.12.2025",
        "comment": "Тестовый комментарий"
    }

    ALL_ORDERS = [ORDER_1, ORDER_2]
