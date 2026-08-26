from .base_page import BasePage
from locators.order_modal_locators import OrderModalLocators

class OrderModal(BasePage):
    def get_order_number(self):
        text = self.get_text(OrderModalLocators.ORDER_NUMBER)
        return text.replace('#', '').strip()

    def close_modal(self):
        element = self.find_element(OrderModalLocators.CLOSE_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_order_modal(self, timeout=10):
        # Ожидает появления модального окна с номером заказа
        self.wait_for_element_visible(OrderModalLocators.ORDER_NUMBER)