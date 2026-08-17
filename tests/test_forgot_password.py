import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from urls import FORGOT_PASSWORD_URL, RESET_PASSWORD_URL


@allure.feature("Восстановление пароля")
class TestForgotPassword:
    @allure.title("Переход на страницу восстановления пароля")
    def test_click_forgot_password_opens_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_forgot_password()

        assert login_page.wait_for_url(FORGOT_PASSWORD_URL) == FORGOT_PASSWORD_URL

    @allure.title("Ввод email и клик «Восстановить» открывают страницу нового пароля")
    def test_enter_email_and_click_restore_opens_reset_password_page(
        self, driver, registered_user
    ):
        forgot_page = ForgotPasswordPage(driver)
        reset_page = ResetPasswordPage(driver)

        forgot_page.open_forgot_password_page()
        forgot_page.enter_email(registered_user["email"])
        forgot_page.click_restore()

        assert forgot_page.get_current_url() == RESET_PASSWORD_URL
        assert reset_page.wait_until_opened()

    @allure.title("Кнопка показать/скрыть пароль активирует поле пароля")
    def test_show_password_button_activates_password_field(
        self, driver, registered_user
    ):
        forgot_page = ForgotPasswordPage(driver)
        reset_page = ResetPasswordPage(driver)

        forgot_page.open_forgot_password_page()
        forgot_page.enter_email(registered_user["email"])
        forgot_page.click_restore()
        reset_page.wait_until_opened()
        reset_page.click_show_hide_password()

        assert reset_page.is_password_field_active()
