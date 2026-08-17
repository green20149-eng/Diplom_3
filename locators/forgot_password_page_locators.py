from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    EMAIL_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Email']/following-sibling::input",
    )
    RESTORE_BUTTON = (By.XPATH, "//button[normalize-space()='Восстановить']")
