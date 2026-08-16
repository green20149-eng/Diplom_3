import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from data import UserData
from pages.login_page import LoginPage
from urls import REGISTER_API_URL, USER_API_URL


@pytest.fixture(params=["chrome", "firefox"], ids=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
            },
        )
        browser = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        browser = webdriver.Firefox(options=options)

    browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()


@pytest.fixture
def registered_user():
    user = UserData.generate_user()
    response = requests.post(REGISTER_API_URL, json=user, timeout=15)

    assert response.status_code == 200, (
        f"Не удалось создать тестового пользователя: "
        f"{response.status_code} {response.text}"
    )

    response_data = response.json()
    user["access_token"] = response_data["accessToken"]

    yield user

    requests.delete(
        USER_API_URL,
        headers={"Authorization": user["access_token"]},
        timeout=15,
    )


@pytest.fixture
def logged_in_user(driver, registered_user):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(registered_user["email"], registered_user["password"])
    return registered_user
