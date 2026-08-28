import allure
from .base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    @allure.step("Получение значения счётчика 'Выполнено за всё время'")
    def get_total_counter_value(self):
        return int(self.get_text(OrderFeedLocators.TOTAL_COUNTER))

    @allure.step("Получение значения счётчика 'Выполнено за сегодня'")
    def get_today_counter_value(self):
        return int(self.get_text(OrderFeedLocators.TODAY_COUNTER))

    @allure.step("Получение списка заказов в разделе 'В работе'")
    def get_orders_in_progress(self):
        elements = self.find_elements(OrderFeedLocators.ORDERS_IN_PROGRESS)
        return [el.text for el in elements]

    @allure.step("Ожидание увеличения счётчика 'Выполнено за всё время' (было {initial_value})")
    def wait_for_total_counter_increase(self, initial_value, timeout=10):
        def counter_changed(driver):
            try:
                current = self.get_total_counter_value()
                return current > initial_value
            except:
                return False
        from selenium.webdriver.support.ui import WebDriverWait
        wait = WebDriverWait(self.driver, timeout)
        wait.until(counter_changed, message="Счётчик 'Выполнено за всё время' не увеличился")

    @allure.step("Ожидание увеличения счётчика 'Выполнено за сегодня' (было {initial_value})")
    def wait_for_today_counter_increase(self, initial_value, timeout=10):
        def counter_changed(driver):
            try:
                current = self.get_today_counter_value()
                return current > initial_value
            except:
                return False
        from selenium.webdriver.support.ui import WebDriverWait
        wait = WebDriverWait(self.driver, timeout)
        wait.until(counter_changed, message="Счётчик 'Выполнено за сегодня' не увеличился")

    @allure.step("Ожидание появления заказа {order_number} в разделе 'В работе'")
    def wait_for_order_in_progress(self, order_number, timeout=20):
        def order_appeared(driver):
            orders = self.get_orders_in_progress()
            return order_number in orders
        from selenium.webdriver.support.ui import WebDriverWait
        wait = WebDriverWait(self.driver, timeout)
        wait.until(order_appeared, message=f"Заказ {order_number} не появился в разделе 'В работе'")