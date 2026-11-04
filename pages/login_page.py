import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    
    @allure.step("Авторизоваться в приложении")
    def login(self, email, password):
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)

        self.wait_for_invisibility(
            (By.CSS_SELECTOR, "div[class*='Modal_modal_overlay__']")
        )

        self.click_element(LoginPageLocators.LOGIN_BUTTON)