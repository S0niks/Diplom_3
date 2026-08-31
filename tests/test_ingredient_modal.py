import allure
import pytest
from data import INGREDIENT_NAME

@allure.feature("Ингредиенты")
class TestIngredientModal:

    @allure.title("Модальное окно ингредиента открывается при клике")
    @allure.story("Открытие модального окна при клике на ингредиент")
    def test_ingredient_modal_opens(self, main_page, ingredient_modal):
        main_page.click_ingredient(INGREDIENT_NAME)
        assert ingredient_modal.is_modal_displayed(), "Модальное окно не открылось"
        assert INGREDIENT_NAME in ingredient_modal.get_ingredient_name()

    @allure.title("Модальное окно ингредиента закрывается по крестику")
    @allure.story("Закрытие модального окна по крестику")
    def test_ingredient_modal_closes(self, main_page, ingredient_modal):
        main_page.click_ingredient(INGREDIENT_NAME)
        assert ingredient_modal.is_modal_displayed()
        ingredient_modal.close_modal()
        ingredient_modal.wait_until_closed()
        assert not ingredient_modal.is_modal_displayed(), "Модальное окно не закрылось"