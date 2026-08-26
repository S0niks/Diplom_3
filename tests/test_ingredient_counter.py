import allure
import pytest
from pages.main_page import MainPage
from data import INGREDIENT_NAME_FILLING

@allure.feature("Конструктор")
class TestIngredientCounter:

    @allure.story("Счётчик ингредиента увеличивается при добавлении")
    def test_ingredient_counter_increases(self, logged_in_browser):
        driver = logged_in_browser
        main = MainPage(driver)
        ingredient_name = INGREDIENT_NAME_FILLING
        # Получаем начальное значение
        try:
            initial = int(main.get_ingredient_counter(ingredient_name))
        except:
            initial = 0
        # Перетаскиваем ингредиент в корзину
        main.drag_and_drop_ingredient(ingredient_name)
        # Ожидаем увеличения счётчика
        main.wait_for_counter_increase(ingredient_name, initial)
        # Доп проверка
        new = int(main.get_ingredient_counter(ingredient_name))
        assert new == initial + 1, f"Счётчик не увеличился: было {initial}, стало {new}"