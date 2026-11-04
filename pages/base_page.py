import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Нажать на элемент")
    def click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step("Найти видимый элемент")
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Дождаться нужного URL")
    def wait_for_url(self, url):
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(url)
        )

    @allure.step("Открыть страницу: {url}")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Обновить страницу")
    def refresh_page(self):
        self.driver.refresh()

    @allure.step("Выполнить JavaScript")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @allure.step("Дождаться появления элемента в DOM")
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Дождаться выполнения условия")
    def wait_for_condition(self, condition):
        return WebDriverWait(self.driver, 10).until(condition)

    @allure.step("Дождаться исчезновения элемента")
    def wait_for_invisibility(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Дождаться корректного номера заказа")
    def wait_for_order_number(self, locator):
        def number_is_ready(driver):
            elements = driver.find_elements(*locator)
            if not elements:
                return False

            number = elements[0].text
            return number if number.isdigit() and number != "9999" else False

        return WebDriverWait(self.driver, 30).until(number_is_ready)

    @allure.step("Дождаться появления текста {expected_text} в элементе")
    def wait_for_text_in_element(self, locator, expected_text, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, expected_text)
        )

    @allure.step("Ввести текст в поле")
    def input_text(self, locator, text):
        self.find_element(locator).send_keys(text)