
import allure

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from urls import Urls


@allure.feature("Основная функциональность")
class TestMainPage:

    @allure.title("Переход в ленту заказов")
    def test_open_order_feed(self, driver):
        main_page = MainPage(driver)

        main_page.open_order_feed()

        with allure.step("Проверить переход в ленту заказов"):
            assert main_page.get_current_url() == Urls.ORDER_FEED_PAGE

    @allure.title("Переход в конструктор")
    def test_open_constructor(self, driver):
        main_page = MainPage(driver)

        main_page.open_order_feed()
        main_page.open_constructor()

        with allure.step("Проверить переход в конструктор"):
            assert main_page.get_current_url().rstrip("/") == Urls.MAIN_PAGE.rstrip("/")

    
    @allure.title("Открытие модального окна ингредиента")
    def test_open_ingredient_details(self, driver):
        main_page = MainPage(driver)

        main_page.open_ingredient_details()

        with allure.step("Проверить открытие модального окна"):
            assert main_page.is_ingredient_modal_open()

        with allure.step("Проверить название ингредиента"):
            assert main_page.get_ingredient_name() == "Краторная булка N-200i"

    
    @allure.title("Закрытие модального окна ингредиента")
    def test_close_ingredient_details(self, driver):
        main_page = MainPage(driver)

        main_page.open_ingredient_details()
        main_page.close_ingredient_details()
        main_page.wait_for_modal_close()

        assert main_page.is_ingredient_modal_closed()

    
    @allure.title("Увеличение счётчика после добавления ингредиента")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)

        with allure.step("Получить начальное значение счётчика"):
            initial_counter = main_page.get_ingredient_counter()

        main_page.add_ingredient()

        with allure.step("Проверить увеличение счётчика"):
            assert main_page.get_ingredient_counter() == initial_counter + 2

