
import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    
    
    @allure.step("Авторизоваться в приложении")
    def login(self, email, password):
        self.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, "div[class*='Modal_modal_overlay__']")
            )
        )

        self.click_element(LoginPageLocators.LOGIN_BUTTON)


