from selenium.webdriver.common.by import By

class OrderModalLocators:
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'Modal_modal__title')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")