import allure

from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from urls import LOGIN_URL, ORDER_HISTORY_URL, PROFILE_URL


@allure.feature("Личный кабинет")
class TestProfile:
    @allure.title("Переход в личный кабинет по клику на «Личный кабинет»")
    def test_click_personal_account_opens_profile(self, driver, logged_in_user):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_personal_account()

        assert main_page.get_current_url() == PROFILE_URL

    @allure.title("Переход в раздел «История заказов»")
    def test_click_order_history_opens_order_history(self, driver, logged_in_user):
        profile_page = ProfilePage(driver)
        profile_page.open_from_header()
        profile_page.open_order_history()

        assert profile_page.get_current_url() == ORDER_HISTORY_URL

    @allure.title("Выход из аккаунта")
    def test_logout_redirects_to_login(self, driver, logged_in_user):
        profile_page = ProfilePage(driver)
        profile_page.open_from_header()
        profile_page.logout()

        assert profile_page.get_current_url() == LOGIN_URL
