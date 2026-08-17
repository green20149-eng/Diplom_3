import allure
from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import BASE_URL, ORDER_FEED_URL, PROFILE_URL


class MainPage(BasePage):
    @allure.step("Открыть конструктор")
    def open_main_page(self):
        self.open(BASE_URL)
        self.is_visible(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step("Перейти в «Конструктор» через шапку")
    def click_constructor(self):
        self.click(HeaderLocators.CONSTRUCTOR_LINK)
        self.wait_for_url(BASE_URL + "/")

    @allure.step("Перейти в «Ленту заказов» через шапку")
    def click_order_feed(self):
        self.click(HeaderLocators.ORDER_FEED_LINK)
        self.wait_for_url(ORDER_FEED_URL)

    @allure.step("Перейти в «Личный кабинет»")
    def click_personal_account(self):
        self.click(HeaderLocators.PERSONAL_ACCOUNT_LINK)
        self.wait_for_url(PROFILE_URL)

    @allure.step("Открыть детали ингредиента")
    def open_target_ingredient(self):
        self.click(MainPageLocators.TARGET_BUN_CARD)

    @allure.step("Проверить, что модальное окно ингредиента открыто")
    def is_ingredient_modal_visible(self):
        return self.is_visible(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверить, что модальное окно ингредиента закрыто")
    def wait_ingredient_modal_closed(self):
        return self.wait_until_invisible(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step("Получить счётчик выбранной булки")
    def get_target_bun_counter(self):
        elements = self.find_elements(MainPageLocators.TARGET_BUN_COUNTER)
        return int(elements[0].text) if elements else 0

    @allure.step("Добавить булку в заказ")
    def add_target_bun_to_order(self):
        before = self.get_target_bun_counter()

        self.drag_and_drop(
            MainPageLocators.TARGET_BUN_CARD,
            MainPageLocators.BUN_DROP_ZONE
        )

        self.wait_until(
            lambda _: self.get_target_bun_counter() > before
        )
        self.close_ingredient_modal_if_open()

    @allure.step("Нажать «Оформить заказ»")
    def click_create_order(self):
        self.click(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Дождаться созданного заказа и получить его номер")
    def get_created_order_number(self):
        self.is_visible(MainPageLocators.ORDER_IDENTIFIER)

        def real_order_number(_):
            text = self.get_text(MainPageLocators.ORDER_NUMBER).strip()
            return text if text.isdigit() and text != "9999" else False

        return self.wait_until(real_order_number)

    @allure.step("Проверить успешное оформление заказа")
    def is_order_created(self):
        return self.is_visible(MainPageLocators.ORDER_STATUS)

    @allure.step("Закрыть модальное окно созданного заказа")
    def close_created_order_modal(self):
        self.close_modal()
        self.wait_until_invisible(MainPageLocators.ORDER_IDENTIFIER)


    @allure.step("Закрыть модальное окно ингредиента, если оно открылось")
    def close_ingredient_modal_if_open(self):
        if self.find_elements(MainPageLocators.INGREDIENT_MODAL_TITLE):
            self.close_modal()
            self.wait_ingredient_modal_closed()

    @allure.step("Дождаться созданного заказа и получить его номер")
    def get_created_order_number(self):
        self.is_visible(MainPageLocators.ORDER_IDENTIFIER)

        def real_order_number(_):
            text = self.get_text(
                MainPageLocators.ORDER_NUMBER
            ).strip()
            if text.isdigit() and text != "9999":
                return self.normalize_order_number(text)
            return False
        return self.wait_until(real_order_number)