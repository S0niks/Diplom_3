from .base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators

class OrderFeedPage(BasePage):
    def get_total_counter_value(self):
        return int(self.get_text(OrderFeedLocators.TOTAL_COUNTER))

    def get_today_counter_value(self):
        return int(self.get_text(OrderFeedLocators.TODAY_COUNTER))

    def get_orders_in_progress(self):
        elements = self.find_elements(OrderFeedLocators.ORDERS_IN_PROGRESS)
        return [el.text for el in elements]

    def wait_for_total_counter_increase(self, initial_value, timeout=10):
        # Ожидает, пока значение счётчика 'Выполнено за всё время' станет больше initial_value
        def counter_changed(driver):
            try:
                current = self.get_total_counter_value()
                return current > initial_value
            except:
                return False
        self.wait.until(counter_changed, message="Счётчик 'Выполнено за всё время' не увеличился")

    def wait_for_today_counter_increase(self, initial_value, timeout=10):
        # Ожидает, пока значение счётчика 'Выполнено за сегодня' станет больше initial_value
        def counter_changed(driver):
            try:
                current = self.get_today_counter_value()
                return current > initial_value
            except:
                return False
        self.wait.until(counter_changed, message="Счётчик 'Выполнено за сегодня' не увеличился")

    def wait_for_order_in_progress(self, order_number, timeout=20):
        # Ожидает появления номера заказа в разделе 'В работе'
        def order_appeared(driver):
            orders = self.get_orders_in_progress()
            return order_number in orders
        self.wait.until(order_appeared, message=f"Заказ {order_number} не появился в разделе 'В работе'")