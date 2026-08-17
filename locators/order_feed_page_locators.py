from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    TITLE = (By.XPATH, "//h1[normalize-space()='Лента заказов']")
    ORDER_LINKS = (By.XPATH, "//a[contains(@class, 'OrderHistory_link')]")
    ORDER_NUMBERS = (
        By.XPATH,
        "//a[contains(@class, 'OrderHistory_link')]"
        "//p[contains(@class, 'text_type_digits-default')][1]",
    )
    ORDER_DETAILS_COMPOSITION = (
        By.XPATH,
        "//*[normalize-space()='Cостав' or normalize-space()='Состав']",
    )
    TOTAL_DONE_COUNTER = (
        By.XPATH,
        "//*[contains(normalize-space(), 'Выполнено за все время')]"
        "/following-sibling::p[1]",
    )
    TODAY_DONE_COUNTER = (
        By.XPATH,
        "//*[contains(normalize-space(), 'Выполнено за сегодня')]"
        "/following-sibling::p[1]",
    )
    IN_PROGRESS_NUMBERS = (
        By.XPATH,
        "//*[contains(normalize-space(), 'В работе')]"
        "/following-sibling::ul[1]/li",
    )
