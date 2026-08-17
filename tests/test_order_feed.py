import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Клик по заказу открывает окно с деталями")
    def test_click_order_opens_order_details(self, driver):
        feed_page = OrderFeedPage(driver)

        feed_page.open_order_feed_page()
        feed_page.open_first_order()

        assert feed_page.is_order_details_visible()

    @allure.title("Созданный заказ отображается в истории заказов")
    def test_created_order_displayed_in_order_history(
            self, driver, registered_user, created_order):
        order_number = created_order
        profile_page = ProfilePage(driver)

        profile_page.open_order_history()

        assert profile_page.wait_for_order(order_number)

    @allure.title("Созданный заказ отображается в ленте заказов")
    def test_created_order_displayed_in_order_feed(
            self, driver, registered_user, created_order):
        order_number = created_order
        profile_page = ProfilePage(driver)

        profile_page.click_order_feed()

        assert profile_page.wait_for_order_in_feed(order_number)

    @allure.title(
        "После создания заказа увеличивается счётчик «Выполнено за всё время»"
    )
    def test_create_order_increases_total_done_counter(
            self, driver, logged_in_user):
        feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)

        feed_page.open_order_feed_page()
        previous_value = feed_page.get_total_done_counter()
        feed_page.click_constructor()

        main_page.add_target_bun_to_order()
        main_page.click_create_order()
        main_page.get_created_order_number()
        main_page.close_created_order_modal()

        main_page.click_order_feed()
        current_value = feed_page.wait_total_counter_increased(previous_value)

        assert current_value > previous_value

    @allure.title(
        "После создания заказа увеличивается счётчик «Выполнено за сегодня»"
    )
    def test_create_order_increases_today_done_counter(
            self, driver, logged_in_user):
        feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)

        feed_page.open_order_feed_page()
        previous_value = feed_page.get_today_done_counter()
        feed_page.click_constructor()

        main_page.add_target_bun_to_order()
        main_page.click_create_order()
        main_page.get_created_order_number()
        main_page.close_created_order_modal()

        main_page.click_order_feed()
        current_value = feed_page.wait_today_counter_increased(previous_value)

        assert current_value > previous_value

    @allure.title("Номер нового заказа появляется в разделе «В работе»")
    def test_created_order_appears_in_progress(
            self, driver, logged_in_user):
        main_page = MainPage(driver)
        feed_page = OrderFeedPage(driver)

        main_page.open_main_page()
        main_page.add_target_bun_to_order()
        main_page.click_create_order()
        order_number = main_page.get_created_order_number()
        main_page.close_created_order_modal()

        main_page.click_order_feed()

        assert feed_page.wait_for_order_in_progress(order_number)
