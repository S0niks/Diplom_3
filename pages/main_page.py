from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def click_constructor(self):
        element = self.find_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    def click_order_feed(self):
        element = self.find_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    def click_personal_account(self):
        element = self.find_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    def click_login_button(self):
        self.click(MainPageLocators.LOGIN_BUTTON)

    def click_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    def click_ingredient(self, name):
        locator = MainPageLocators.ingredient_by_name(name)
        self.click(locator)

    def drag_and_drop_ingredient(self, name):
        ingredient = self.find_element(MainPageLocators.ingredient_by_name(name))
        target = self.find_element(MainPageLocators.BUN_CONSTRUCTOR)
        # JavaScript-эмуляция drag-and-drop
        self.driver.execute_script("""
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

    def get_ingredient_counter(self, name):
        locator = MainPageLocators.ingredient_counter(name)
        return self.find_element(locator).text

    def wait_for_counter_increase(self, name, initial_value, timeout=10):
        def counter_changed(driver):
            try:
                current = int(self.get_ingredient_counter(name))
                return current > initial_value
            except:
                return False
        self.wait.until(counter_changed, message=f"Счётчик для {name} не увеличился")