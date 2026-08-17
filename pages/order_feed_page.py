import allure

from locators.header_locators import HeaderLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage
from urls import BASE_URL, ORDER_FEED_URL


class OrderFeedPage(BasePage):
    @allure.step("Открыть ленту заказов")
    def open_order_feed_page(self):
        self.open(ORDER_FEED_URL)
        self.is_visible(OrderFeedPageLocators.TITLE)

    @allure.step("Открыть первый заказ в ленте")
    def open_first_order(self):
        self.click(OrderFeedPageLocators.ORDER_LINKS)

    @allure.step("Проверить открытие деталей заказа")
    def is_order_details_visible(self):
        return self.is_visible(OrderFeedPageLocators.ORDER_DETAILS_COMPOSITION)

    @allure.step("Получить номера заказов из ленты")
    def get_order_numbers(self):
        return [text.lstrip("#").strip() for text in self.get_texts(OrderFeedPageLocators.ORDER_NUMBERS)]

    @allure.step("Дождаться заказа №{order_number} в ленте")
    def wait_for_order(self, order_number):
        expected_number = self.normalize_order_number(
            order_number
        )

        def order_is_present(_):
            elements = self.find_elements(
                OrderFeedPageLocators.ORDER_NUMBERS
            )

            numbers = [
                self.normalize_order_number(element.text)
                for element in elements
                if element.text.strip()
            ]
            return expected_number in numbers
        return self.wait_until(order_is_present)

    @allure.step("Получить счётчик «Выполнено за всё время»")
    def get_total_done_counter(self):
        return int(self.get_text(OrderFeedPageLocators.TOTAL_DONE_COUNTER).replace(" ", ""))

    @allure.step("Получить счётчик «Выполнено за сегодня»")
    def get_today_done_counter(self):
        return int(self.get_text(OrderFeedPageLocators.TODAY_DONE_COUNTER).replace(" ", ""))

    @allure.step("Дождаться увеличения общего счётчика")
    def wait_total_counter_increased(self, previous_value):
        return self.wait_until(
            lambda _: self.get_total_done_counter()
            if self.get_total_done_counter() > previous_value
            else False
        )

    @allure.step("Дождаться увеличения сегодняшнего счётчика")
    def wait_today_counter_increased(self, previous_value):
        return self.wait_until(
            lambda _: self.get_today_done_counter()
            if self.get_today_done_counter() > previous_value
            else False
        )

    @allure.step("Дождаться заказа №{order_number} в разделе «В работе»")
    def wait_for_order_in_progress(self, order_number):
        expected_number = self.normalize_order_number(
            order_number
        )
        def order_is_in_progress(_):
            elements = self.find_elements(
                OrderFeedPageLocators.IN_PROGRESS_NUMBERS
            )
            numbers = [
                self.normalize_order_number(element.text)
                for element in elements
                if element.text.strip()
            ]
            return expected_number in numbers
        return self.wait_until(order_is_in_progress)

    @allure.step("Перейти в конструктор")
    def click_constructor(self):
        self.click(HeaderLocators.CONSTRUCTOR_LINK)
        self.wait_for_url(BASE_URL + "/")
