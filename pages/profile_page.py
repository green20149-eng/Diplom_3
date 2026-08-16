import allure

from locators.header_locators import HeaderLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage
from urls import LOGIN_URL, ORDER_FEED_URL, ORDER_HISTORY_URL, PROFILE_URL


class ProfilePage(BasePage):
    @allure.step("Открыть личный кабинет через шапку")
    def open_from_header(self):
        self.click(HeaderLocators.PERSONAL_ACCOUNT_LINK)
        self.wait_for_url(PROFILE_URL)
        self.is_visible(ProfilePageLocators.PROFILE_INFO)

    @allure.step("Перейти в историю заказов")
    def open_order_history(self):
        self.click(ProfilePageLocators.ORDER_HISTORY_LINK)
        self.wait_for_url(ORDER_HISTORY_URL)

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)
        self.wait_for_url(LOGIN_URL)

    @allure.step("Получить номера заказов из истории")
    def get_order_numbers(self):
        return [text.lstrip("#").strip() for text in self.get_texts(ProfilePageLocators.ORDER_NUMBERS)]

    @allure.step("Дождаться заказа №{order_number} в истории")
    def wait_for_order(self, order_number):
        def order_is_present(_):
            elements = self.find_elements(ProfilePageLocators.ORDER_NUMBERS)
            numbers = [element.text.lstrip("#").strip() for element in elements]
            return order_number in numbers

        return self.wait_until(order_is_present)

    @allure.step("Перейти из личного кабинета в ленту заказов")
    def click_order_feed(self):
        self.click(HeaderLocators.ORDER_FEED_LINK)
        self.wait_for_url(ORDER_FEED_URL)

    @allure.step("Дождаться заказа №{order_number} в истории")
    def wait_for_order(self, order_number):
        expected_number = self.normalize_order_number(
            order_number
        )

        def order_is_present(_):
            elements = self.find_elements(
                ProfilePageLocators.ORDER_NUMBERS
            )
            numbers = [
                self.normalize_order_number(element.text)
                for element in elements
                if element.text.strip()
            ]
            return expected_number in numbers
        return self.wait_until(order_is_present)
