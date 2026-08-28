from .base_page import BasePage
from locators.ingredient_modal_locators import IngredientModalLocators
import allure

class IngredientModal(BasePage):
    @allure.step("Проверка отображения модального окна ингредиента")
    def is_modal_displayed(self):
        try:
            return self.find_element(IngredientModalLocators.MODAL_ROOT).is_displayed()
        except:
            return False

    @allure.step("Закрытие модального окна ингредиента")
    def close_modal(self):
        self.click(IngredientModalLocators.CLOSE_BUTTON)

    @allure.step("Получение названия ингредиента из модального окна")
    def get_ingredient_name(self):
        return self.get_text(IngredientModalLocators.INGREDIENT_NAME)