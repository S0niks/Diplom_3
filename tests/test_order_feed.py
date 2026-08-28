import allure
import pytest
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.order_modal import OrderModal
from data import INGREDIENT_NAME, INGREDIENT_NAME_FILLING

@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Счётчик 'Выполнено за всё время' увеличивается после создания заказа")
    @allure.story("Счётчик 'Выполнено за всё время' увеличивается после создания заказа")
    def test_total_counter_increases(self, logged_in_browser):
        driver = logged_in_browser
        main = MainPage(driver)
        # Переходим в ленту заказов, чтобы получить начальное значение
        main.click_order_feed()
        feed = OrderFeedPage(driver)
        initial_total = feed.get_total_counter_value()
        # Возвращаемся в конструктор
        main.click_constructor()
        # Добавляем ингредиенты перетаскиванием
        main.drag_and_drop_ingredient(INGREDIENT_NAME)
        main.drag_and_drop_ingredient(INGREDIENT_NAME_FILLING)
        # Оформляем заказ
        main.click_order_button()
        order_modal = OrderModal(driver)
        # Ждём появления модалки с номером заказа
        order_modal.wait_for_order_modal()
        # Закрываем модалку
        order_modal.close_modal()
        # Переходим в ленту
        main.click_order_feed()
        # Ожидаем увеличения счётчика
        feed.wait_for_total_counter_increase(initial_total)
        # Проверяем финальное значение
        new_total = feed.get_total_counter_value()
        assert new_total > initial_total, "Счётчик не увеличился"

    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается после создания заказа")
    @allure.story("Счётчик 'Выполнено за сегодня' увеличивается после создания заказа")
    def test_today_counter_increases(self, logged_in_browser):
        driver = logged_in_browser
        main = MainPage(driver)
        main.click_order_feed()
        feed = OrderFeedPage(driver)
        initial_today = feed.get_today_counter_value()
        main.click_constructor()
        main.drag_and_drop_ingredient(INGREDIENT_NAME)
        main.drag_and_drop_ingredient(INGREDIENT_NAME_FILLING)
        main.click_order_button()
        order_modal = OrderModal(driver)
        order_modal.wait_for_order_modal()
        order_modal.close_modal()
        main.click_order_feed()
        feed.wait_for_today_counter_increase(initial_today)
        new_today = feed.get_today_counter_value()
        assert new_today > initial_today, "Счётчик 'Выполнено за сегодня' не увеличился"

    @allure.title("Номер созданного заказа отображается в разделе 'В работе'")
    @allure.story("Номер заказа появляется в разделе 'В работе'")
    def test_order_number_in_progress(self, logged_in_browser):
        driver = logged_in_browser
        main = MainPage(driver)
        main.click_constructor()
        main.drag_and_drop_ingredient(INGREDIENT_NAME)
        main.drag_and_drop_ingredient(INGREDIENT_NAME_FILLING)
        main.click_order_button()
        order_modal = OrderModal(driver)
        order_modal.wait_for_order_modal()
        order_number = order_modal.get_order_number()
        order_modal.close_modal()
        main.click_order_feed()
        feed = OrderFeedPage(driver)
        # Ожидаем появления номера в списке "В работе"
        feed.wait_for_order_in_progress(order_number)
        # Доп проверка
        assert order_number in feed.get_orders_in_progress(), f"Номер {order_number} не найден"