import allure
from pages.login_page import LoginPage
from urls import Urls


@allure.feature("Авторизация")
class TestLogin:

    @allure.title("Авторизация временного пользователя")
    def test_login(self, driver, authorized_user):
        login_page = LoginPage(driver)

        with allure.step("Проверить переход на главную страницу"):
            assert login_page.get_current_url().rstrip("/") == Urls.MAIN_PAGE.rstrip("/")