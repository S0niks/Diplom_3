from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@href,'/')]//p[text()='Конструктор']/..")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[contains(@href,'/feed')]//p[text()='Лента Заказов']/..")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href,'/account')]//p[text()='Личный Кабинет']/..")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    BUN_CONSTRUCTOR = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    
    # Локатор для ингредиента по имени
    @staticmethod
    def ingredient_by_name(name):
        return (By.XPATH, f"//p[text()='{name}']/ancestor::a")
    
    # Счётчик ингредиента
    @staticmethod
    def ingredient_counter(name):
        return (By.XPATH, f"//*[text()='{name}']/ancestor::a//div[contains(@class, 'counter')]")