
import allure
from urls import Urls


@allure.feature("Авторизация")
class TestLogin:

    @allure.title("Авторизация временного пользователя")
    def test_login(self, driver, authorized_user):
        with allure.step("Проверить переход на главную страницу"):
            assert driver.current_url.rstrip("/") == Urls.MAIN_PAGE.rstrip("/")
