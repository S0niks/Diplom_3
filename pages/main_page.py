import allure
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class MainPage(BasePage):

    @allure.step("Переход на страницу Конструктора")
    def click_constructor(self):
        element = self.find_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.execute_script("arguments[0].click();", element)

    @allure.step("Переход на страницу Ленты заказов")
    def click_order_feed(self):
        element = self.find_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.execute_script("arguments[0].click();", element)

    @allure.step("Переход в Личный кабинет")
    def click_personal_account(self):
        element = self.find_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.execute_script("arguments[0].click();", element)

    @allure.step("Клик по кнопке 'Войти'")
    def click_login_button(self):
        self.click(MainPageLocators.LOGIN_BUTTON)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    @allure.step("Клик по ингредиенту: {name}")
    def click_ingredient(self, name):
        locator = MainPageLocators.ingredient_by_name(name)
        self.click(locator)

    @allure.step("Добавление ингредиента '{name}' в заказ (drag-and-drop)")
    def drag_and_drop_ingredient(self, name):
        ingredient = self.find_element(MainPageLocators.ingredient_by_name(name))
        target = self.find_element(MainPageLocators.BUN_CONSTRUCTOR)
        # JavaScript-эмуляция drag-and-drop
        self.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, ingredient, target)

    @allure.step("Получение текста счётчика ингредиента: {name}")
    def get_ingredient_counter(self, name):
        locator = MainPageLocators.ingredient_counter(name)
        return self.find_element(locator).text

    @allure.step("Получение числового значения счётчика ингредиента: {name}")
    def get_ingredient_counter_value(self, name):
        """Возвращает числовое значение счётчика ингредиента, или 0, если счётчик отсутствует."""
        try:
            return int(self.get_ingredient_counter(name))
        except NoSuchElementException:
            return 0

    @allure.step("Ожидание увеличения счётчика ингредиента: {name} (было {initial_value})")
    def wait_for_counter_increase(self, name, initial_value, timeout=10):
        def counter_changed(driver):
            try:
                current = int(self.get_ingredient_counter(name))
                return current > initial_value
            except:
                return False
        self.wait_until(counter_changed, timeout=timeout, message=f"Счётчик для {name} не увеличился")