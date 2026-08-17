from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_LINK = (By.LINK_TEXT, "Профиль")
    ORDER_HISTORY_LINK = (By.LINK_TEXT, "История заказов")
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выход']")
    PROFILE_INFO = (
        By.XPATH,
        "//*[contains(normalize-space(), 'персональные данные')]",
    )
    ORDER_NUMBERS = (
        By.XPATH,
        "//a[contains(@class, 'OrderHistory_link')]"
        "//p[contains(@class, 'text_type_digits-default')][1]",
    )
