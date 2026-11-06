import requests
from helpers import Helpers
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from urls import Urls


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()

    browser.maximize_window()
    browser.get(Urls.MAIN_PAGE)

    yield browser

    browser.quit()


@pytest.fixture
def created_user():
    user_data = Helpers.generate_user_data()

    response = requests.post(
        Urls.REGISTER_URL,
        json=user_data,
        timeout=10
    )
    response.raise_for_status()

    access_token = response.json()["accessToken"]

    yield user_data, access_token

    requests.delete(
        Urls.USER_URL,
        headers={"Authorization": access_token},
        timeout=10
    )



@pytest.fixture
def authorized_user(driver, created_user):
    user_data, access_token = created_user

    response = requests.post(
        Urls.LOGIN_URL,
        json={
            "email": user_data["email"],
            "password": user_data["password"]
        },
        timeout=10
    )
    response.raise_for_status()

    tokens = response.json()
    login_page = LoginPage(driver)

    login_page.execute_script(
        "window.localStorage.setItem('accessToken', arguments[0]);",
        tokens["accessToken"]
    )
    login_page.execute_script(
        "window.localStorage.setItem('refreshToken', arguments[0]);",
        tokens["refreshToken"]
    )

    login_page.refresh_page()

    return user_data



