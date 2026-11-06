
from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//p[text()='Конструктор']/parent::a"
    )

    ORDER_FEED_BUTTON = (
        By.XPATH,
        "//p[text()='Лента Заказов']/parent::a"
    )

    INGREDIENT_NAME_IN_MODAL = (
        By.CSS_SELECTOR,
        "p.text_type_main-medium.mb-8"
    )

    CLOSE_MODAL_BUTTON = (
        By.CSS_SELECTOR,
        "button[class*='Modal_modal__close__']"
    )

    INGREDIENT_CARD = (
        By.XPATH,
        "//a[.//p[text()='Краторная булка N-200i']]"
    )

    INGREDIENT_COUNTER = (
        By.XPATH,
        "//a[.//p[text()='Краторная булка N-200i']]"
        "//div[contains(@class, 'counter_counter__')]//p"
    )

    CONSTRUCTOR_DROP_AREA = (
        By.XPATH,
        "//div[contains(@class, 'constructor-element_pos_top')]"
        "[.//span[text()='Перетяните булочку сюда (верх)']]"
    )

    CREATE_ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Оформить заказ']"
    )

    ORDER_NUMBER = (
        By.CSS_SELECTOR,
        "h2[class*='Modal_modal__title__']"
    )