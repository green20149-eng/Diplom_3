import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage
from urls import FORGOT_PASSWORD_URL, RESET_PASSWORD_URL


class ForgotPasswordPage(BasePage):
    @allure.step("Открыть страницу восстановления пароля")
    def open_forgot_password_page(self):
        self.open(FORGOT_PASSWORD_URL)
        self.is_visible(ForgotPasswordPageLocators.EMAIL_INPUT)

    @allure.step("Ввести email для восстановления пароля")
    def enter_email(self, email):
        self.type_text(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step("Нажать кнопку «Восстановить»")
    def click_restore(self):
        self.click(ForgotPasswordPageLocators.RESTORE_BUTTON)
        self.wait_for_url(RESET_PASSWORD_URL)
