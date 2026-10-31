
import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Перейти в конструктор")
    def open_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Перейти в ленту заказов")
    def open_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Открыть детали ингредиента")
    def open_ingredient_details(self):
        self.click_element(MainPageLocators.INGREDIENT_CARD)

    @allure.step("Получить название ингредиента в модальном окне")
    def get_ingredient_name(self):
        return self.get_text(MainPageLocators.INGREDIENT_NAME_IN_MODAL)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_details(self):
        self.click_element(MainPageLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Проверить отображение модального окна")
    def is_ingredient_modal_open(self):
        return self.find_element(
            MainPageLocators.CLOSE_MODAL_BUTTON
        ).is_displayed()

    @allure.step("Дождаться закрытия модального окна")
    def wait_for_modal_close(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(
                MainPageLocators.CLOSE_MODAL_BUTTON
            )
        )

    @allure.step("Получить значение счётчика ингредиента")
    def get_ingredient_counter(self):
        return int(self.get_text(MainPageLocators.INGREDIENT_COUNTER))

    
    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient(self):
        ingredient = self.find_element(MainPageLocators.INGREDIENT_CARD)
        drop_area = self.find_element(MainPageLocators.CONSTRUCTOR_DROP_AREA)

        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragenter', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            source.dispatchEvent(new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));
        """, ingredient, drop_area)


    @allure.step("Проверить, что модальное окно закрыто")
    def is_ingredient_modal_closed(self):
        return EC.invisibility_of_element_located(
            MainPageLocators.CLOSE_MODAL_BUTTON
        )(self.driver)

    
    @allure.step("Оформить заказ")
    def create_order(self):
        overlays = self.driver.find_elements(
            By.CSS_SELECTOR,
            "div[class*='Modal_modal_overlay__']"
        )

        self.click_element(MainPageLocators.CREATE_ORDER_BUTTON)


    @allure.step("Получить номер созданного заказа")
    def get_order_number(self):
        WebDriverWait(self.driver, 30).until(
            lambda driver: (
                self.get_text(MainPageLocators.ORDER_NUMBER).isdigit()
                and self.get_text(MainPageLocators.ORDER_NUMBER) != "9999"
            )
        )

        return self.get_text(MainPageLocators.ORDER_NUMBER)

    
    @allure.step("Создать заказ и получить его номер")
    def place_order(self):
        self.add_ingredient()
        self.create_order()
        return self.get_order_number()
