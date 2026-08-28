import allure
import pytest
from pages.main_page import MainPage
from data import INGREDIENT_NAME_FILLING


@allure.feature("Конструктор")
class TestIngredientCounter:

    @allure.title("Счётчик ингредиента увеличивается после добавления в заказ")
    @allure.story("Счётчик ингредиента увеличивается при добавлении")
    def test_ingredient_counter_increases(self, logged_in_browser):
        driver = logged_in_browser
        main = MainPage(driver)
        ingredient_name = INGREDIENT_NAME_FILLING
        # Получаем начальное значение счётчика (0, если элемент не найден)
        initial = main.get_ingredient_counter_value(ingredient_name)
        # Перетаскиваем ингредиент в корзину
        main.drag_and_drop_ingredient(ingredient_name)
        # Ожидаем увеличения счётчика
        main.wait_for_counter_increase(ingredient_name, initial)
        # Проверяем финальное значение
        new = main.get_ingredient_counter_value(ingredient_name)
        assert new == initial + 1, f"Счётчик не увеличился: было {initial}, стало {new}"