
import allure
import pytest
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from urls import Urls


@pytest.fixture
def order_feed_pages(driver, authorized_user):
    main_page = MainPage(driver)
    order_feed_page = OrderFeedPage(driver)
    order_feed_page.open_page(Urls.ORDER_FEED_PAGE)
    return main_page, order_feed_page


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Увеличение счётчика заказов за всё время")
    def test_total_orders_counter_increases(self, order_feed_pages):
        main_page, order_feed_page = order_feed_pages

        with allure.step("Получить количество заказов до оформления"):
            initial_count = order_feed_page.get_total_orders()

        with allure.step("Создать новый заказ"):
            main_page.open_page(Urls.MAIN_PAGE)
            main_page.place_order()

        with allure.step("Проверить увеличение счётчика"):
            order_feed_page.open_page(Urls.ORDER_FEED_PAGE)
            assert order_feed_page.get_total_orders() > initial_count

    @allure.title("Увеличение счётчика заказов за сегодня")
    def test_today_orders_counter_increases(self, order_feed_pages):
        main_page, order_feed_page = order_feed_pages

        with allure.step("Получить количество заказов за сегодня"):
            initial_count = order_feed_page.get_today_orders()

        with allure.step("Создать новый заказ"):
            main_page.open_page(Urls.MAIN_PAGE)
            main_page.place_order()

        with allure.step("Проверить увеличение счётчика"):
            order_feed_page.open_page(Urls.ORDER_FEED_PAGE)
            assert order_feed_page.get_today_orders() > initial_count

    @allure.title("Новый заказ появляется в разделе «В работе»")
    def test_order_appears_in_progress(self, driver, authorized_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Создать заказ и получить его номер"):
            main_page.open_page(Urls.MAIN_PAGE)
            order_number = main_page.place_order()

        with allure.step("Открыть ленту заказов"):
            order_feed_page.open_page(Urls.ORDER_FEED_PAGE)

        with allure.step("Проверить номер заказа в разделе «В работе»"):
            order_feed_page.wait_for_order_in_progress(order_number)
            orders = order_feed_page.get_orders_in_progress().splitlines()
            assert str(order_number).zfill(5) in [
                number.strip() for number in orders
            ]
