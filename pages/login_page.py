import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import BASE_URL, LOGIN_URL


class LoginPage(BasePage):
    @allure.step("Открыть страницу входа")
    def open_login_page(self):
        self.open(LOGIN_URL)
        self.is_visible(LoginPageLocators.TITLE)

    @allure.step("Нажать «Восстановить пароль»")
    def click_forgot_password(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Авторизоваться пользователем")
    def login(self, email, password):
        self.type_text(LoginPageLocators.EMAIL_INPUT, email)
        self.type_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_url(BASE_URL + "/")
