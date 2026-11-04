import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    @allure.step("Получить количество заказов за всё время")
    def get_total_orders(self):
        return int(self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNTER))

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders(self):
        return int(self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNTER))

    @allure.step("Получить номера заказов в работе")
    def get_orders_in_progress(self):
        return self.get_text(OrderFeedLocators.ORDERS_IN_PROGRESS)

    @allure.step("Дождаться появления номера заказа в работе")
    def wait_for_order_in_progress(self, order_number):
        expected_number = str(order_number).zfill(5)

        return self.wait_for_text_in_element(
            OrderFeedLocators.ORDERS_IN_PROGRESS,
            expected_number
        )