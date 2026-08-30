from .base_page import BasePage
from locators.order_modal_locators import OrderModalLocators
import allure

class OrderModal(BasePage):
    @allure.step("Получение номера заказа из модального окна")
    def get_order_number(self):
        text = self.get_text(OrderModalLocators.ORDER_NUMBER)
        return text.replace('#', '').strip()

    @allure.step("Закрытие модального окна заказа")
    def close_modal(self):
        element = self.find_element(OrderModalLocators.CLOSE_BUTTON)
        self.execute_script("arguments[0].click();", element)

    @allure.step("Ожидание появления модального окна с номером заказа")
    def wait_for_order_modal(self, timeout=10):
        self.wait_for_element_visible(OrderModalLocators.ORDER_NUMBER)