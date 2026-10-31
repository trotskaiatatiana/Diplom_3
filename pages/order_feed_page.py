
import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        expected_number = order_number.zfill(4)

        WebDriverWait(self.driver, 30).until(
            lambda driver: expected_number in (
                self.get_orders_in_progress().splitlines()
            )
        )

