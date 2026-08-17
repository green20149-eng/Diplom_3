import allure

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    @allure.step("Дождаться страницы ввода нового пароля")
    def wait_until_opened(self):
        return self.is_visible(ResetPasswordPageLocators.SAVE_BUTTON)

    @allure.step("Нажать кнопку показать/скрыть пароль")
    def click_show_hide_password(self):
        self.click(ResetPasswordPageLocators.SHOW_HIDE_PASSWORD_BUTTON)

    @allure.step("Проверить, что поле пароля активно")
    def is_password_field_active(self):
        return self.is_visible(ResetPasswordPageLocators.ACTIVE_PASSWORD_CONTAINER)
