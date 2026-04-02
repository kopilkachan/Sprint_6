from selenium.webdriver.common.by import By


class HomePageLocators:

    Q_PRICE = (By.ID, "accordion__heading-0")
    Q_MANY_CSOOTERS = (By.ID, "accordion__heading-1")
    Q_TIME = (By.ID, "accordion__heading-2")
    Q_ORDER_TODAY = (By.ID, "accordion__heading-3")
    Q_EXTEND_SHORTEN = (By.ID, "accordion__heading-4")
    Q_CHARGE = (By.ID, "accordion__heading-5")
    Q_CANCEL = (By.ID, "accordion__heading-6")
    Q_MKAD = (By.ID, "accordion__heading-7")

    A_PRICE = (By.XPATH, ".//p[text() = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")
    A_MANY_CSOOTERS = (By.XPATH, ".//p[text() = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']")
    A_TIME = (By.XPATH, ".//p[text() = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']")
    A_ORDER_TODAY = (By.XPATH, ".//p[text() = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")
    A_EXTEND_SHORTEN = (By.XPATH, ".//p[text() = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']")
    A_CHARGE = (By.XPATH, ".//p[text() = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']")
    A_CANCEL = (By.XPATH, ".//p[text() = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']")
    A_MKAD = (By.XPATH, ".//p[text() = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']")

    HEADER_ORDER_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g']")
    BIG_ORDER_BUTTON = (By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[text() = 'Заказать']")
    HEADER_LOGO_SCOOTER = (By.XPATH, ".//img[@alt='Scooter']")
    HEADER_LOGO_YNDX = (By.XPATH, ".//img[@alt='Yandex']")
