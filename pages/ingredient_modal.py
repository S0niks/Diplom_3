from .base_page import BasePage
from locators.ingredient_modal_locators import IngredientModalLocators

class IngredientModal(BasePage):
    def is_modal_displayed(self):
        try:
            return self.find_element(IngredientModalLocators.MODAL_ROOT).is_displayed()
        except:
            return False

    def close_modal(self):
        self.click(IngredientModalLocators.CLOSE_BUTTON)

    def get_ingredient_name(self):
        return self.get_text(IngredientModalLocators.INGREDIENT_NAME)