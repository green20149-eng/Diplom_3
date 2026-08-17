from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    SHOW_HIDE_PASSWORD_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'icon-action') or contains(@class, 'input__icon')]",
    )
    ACTIVE_PASSWORD_CONTAINER = (By.CSS_SELECTOR, ".input.input_status_active")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Сохранить']")
