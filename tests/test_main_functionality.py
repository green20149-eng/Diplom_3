import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from urls import BASE_URL, ORDER_FEED_URL


@allure.feature("Основной функционал")
class TestMainFunctionality:
    @allure.title("Переход в конструктор по клику на «Конструктор»")
    def test_click_constructor_opens_constructor(self, driver):
        feed_page = OrderFeedPage(driver)
        feed_page.open_order_feed_page()
        feed_page.click_constructor()

        assert feed_page.get_current_url() == BASE_URL + "/"

    @allure.title("Переход в ленту заказов по клику на «Лента заказов»")
    def test_click_order_feed_opens_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_order_feed()

        assert main_page.get_current_url() == ORDER_FEED_URL

    @allure.title("Клик по ингредиенту открывает окно с деталями")
    def test_click_ingredient_opens_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.open_target_ingredient()

        assert main_page.is_ingredient_modal_visible()

    @allure.title("Модальное окно ингредиента закрывается по крестику")
    def test_close_button_closes_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.open_target_ingredient()
        main_page.close_modal()

        assert main_page.wait_ingredient_modal_closed()

    @allure.title("Добавление ингредиента увеличивает его счётчик")
    def test_add_ingredient_increases_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        before = main_page.get_target_bun_counter()

        main_page.add_target_bun_to_order()
        after = main_page.get_target_bun_counter()

        assert after > before

    @allure.title("Авторизованный пользователь может оформить заказ")
    def test_authorized_user_can_create_order(self, driver, logged_in_user):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.add_target_bun_to_order()
        main_page.click_create_order()

        order_number = main_page.get_created_order_number()

        assert order_number.isdigit()
        assert main_page.is_order_created()
