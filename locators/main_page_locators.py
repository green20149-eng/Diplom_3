from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_TITLE = (
        By.XPATH,
        "//h1[normalize-space()='Соберите бургер']"
    )

    TARGET_BUN_NAME = "Флюоресцентная булка R2-D3"

    TARGET_BUN_TEXT = (
        By.XPATH,
        f"//p[normalize-space()='{TARGET_BUN_NAME}']",
    )

    # Вся карточка ингредиента, которую можно перетаскивать
    TARGET_BUN_CARD = (
        By.XPATH,
        f"//p[normalize-space()='{TARGET_BUN_NAME}']"
        "/ancestor::*[@draggable='true'][1]",
    )

    TARGET_BUN_COUNTER = (
        By.XPATH,
        f"//p[normalize-space()='{TARGET_BUN_NAME}']/ancestor::a[1]"
        "//*[contains(@class, 'counter') and contains(@class, 'num')]",
    )

    BUN_DROP_ZONE = (
        By.XPATH,
        "//*[normalize-space()='Перетяните булочку сюда (низ)']",
    )

    INGREDIENT_MODAL_TITLE = (
        By.XPATH,
        "//h2[normalize-space()='Детали ингредиента']",
    )

    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Modal_modal__close') "
        "or contains(@class, 'modal__close')]",
    )

    CREATE_ORDER_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Оформить заказ']"
    )

    ORDER_IDENTIFIER = (
        By.XPATH,
        "//*[normalize-space()='идентификатор заказа']",
    )

    ORDER_NUMBER = (
        By.XPATH,
        "(//*[contains(@class, 'Modal_modal__title_shadow')] | "
        "//*[normalize-space()='идентификатор заказа']"
        "/preceding-sibling::*[1])[1]",
    )

    ORDER_STATUS = (
        By.XPATH,
        "//*[contains(normalize-space(), "
        "'Ваш заказ начали готовить')]",
    )