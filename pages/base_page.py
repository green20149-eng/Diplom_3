import allure
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.common_locators import CommonLocators


class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Нажать на элемент")
    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

    @allure.step("Ввести текст")
    def type_text(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    @allure.step("Получить тексты элементов")
    def get_texts(self, locator):
        elements = self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )
        return [element.text for element in elements]

    @allure.step("Проверить отображение элемента")
    def is_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()

    @allure.step("Дождаться исчезновения элемента")
    def wait_until_invisible(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Дождаться URL {url}")
    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))
        return self.driver.current_url

    @allure.step("Получить элементы")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Перетащить элемент")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait.until(
            EC.visibility_of_element_located(source_locator)
        )
        target = self.wait.until(
            EC.visibility_of_element_located(target_locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            source
        )

        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();

            const sourceRect = source.getBoundingClientRect();
            const targetRect = target.getBoundingClientRect();

            function fireDragEvent(element, type, x, y) {
                const event = new DragEvent(type, {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer,
                    clientX: x,
                    clientY: y
                });

                element.dispatchEvent(event);
            }

            const sourceX =
                sourceRect.left + sourceRect.width / 2;
            const sourceY =
                sourceRect.top + sourceRect.height / 2;

            const targetX =
                targetRect.left + targetRect.width / 2;
            const targetY =
                targetRect.top + targetRect.height / 2;

            fireDragEvent(source, 'dragstart', sourceX, sourceY);
            fireDragEvent(target, 'dragenter', targetX, targetY);
            fireDragEvent(target, 'dragover', targetX, targetY);
            fireDragEvent(target, 'drop', targetX, targetY);
            fireDragEvent(source, 'dragend', targetX, targetY);
            """,
            source,
            target
        )

    @allure.step("Дождаться выполнения условия")
    def wait_until(self, condition):
        return self.wait.until(condition)

    @staticmethod
    def normalize_order_number(value):
        value = value.replace("#", "").strip()
        return str(int(value))