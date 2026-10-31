
import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from urls import Urls


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Увеличение счётчика заказов за всё время")
    def test_total_orders_counter_increases(self, driver, authorized_user):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)

        with allure.step("Получить количество заказов до оформления"):
            driver.get(Urls.ORDER_FEED_PAGE)
            initial_count = order_feed_page.get_total_orders()

        with allure.step("Создать новый заказ"):
            driver.get(Urls.MAIN_PAGE)
            main_page.place_order()

        with allure.step("Проверить увеличение счётчика"):
            driver.get(Urls.ORDER_FEED_PAGE)
            assert order_feed_page.get_total_orders() > initial_count

    
    @allure.title("Увеличение счётчика заказов за сегодня")
    def test_today_orders_counter_increases(self, driver, authorized_user):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)

        with allure.step("Получить количество заказов за сегодня"):
            driver.get(Urls.ORDER_FEED_PAGE)
            initial_count = order_feed_page.get_today_orders()

        with allure.step("Создать новый заказ"):
            driver.get(Urls.MAIN_PAGE)
            main_page.place_order()

        with allure.step("Проверить увеличение счётчика"):
            driver.get(Urls.ORDER_FEED_PAGE)
            assert order_feed_page.get_today_orders() > initial_count

    
    @allure.title("Новый заказ появляется в разделе «В работе»")
    def test_order_appears_in_progress(self, driver, authorized_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Создать заказ и получить его номер"):
            order_number = main_page.place_order()

        with allure.step("Открыть ленту заказов"):
            driver.get(Urls.ORDER_FEED_PAGE)

        with allure.step("Проверить номер заказа в разделе «В работе»"):
            order_feed_page.wait_for_order_in_progress(order_number)
