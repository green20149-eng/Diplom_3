from selenium.webdriver.common.by import By


class HeaderLocators:
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//a[@href='/' and .//*[normalize-space()='Конструктор']]",
    )
    ORDER_FEED_LINK = (
        By.XPATH,
        "//a[@href='/feed' and .//*[contains(normalize-space(), 'Лента')]]",
    )
    PERSONAL_ACCOUNT_LINK = (
        By.XPATH,
        "//a[contains(@href, '/account') and .//*[contains(normalize-space(), 'Личный')]]",
    )
