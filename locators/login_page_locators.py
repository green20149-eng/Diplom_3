from selenium.webdriver.common.by import By


class LoginPageLocators:
    TITLE = (By.XPATH, "//h2[normalize-space()='Вход']")
    EMAIL_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Email']/following-sibling::input",
    )
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")
