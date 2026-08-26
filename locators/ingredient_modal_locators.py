from selenium.webdriver.common.by import By

class IngredientModalLocators:
    MODAL_ROOT = (By.XPATH, "//div[contains(@class,'Modal_modal__content')]")
    MODAL_TITLE = (By.XPATH, "//h2[contains(@class,'Modal_modal__title')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
    INGREDIENT_NAME = (By.XPATH, "//div[contains(@class, 'Modal_modal__content')]//p[contains(@class, 'text_type_main-medium')]")