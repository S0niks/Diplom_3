
import allure
import pytest
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

@allure.feature("Навигация")
class TestNavigation:

    @allure.story("Переход на Конструктор")
    def test_click_constructor(self, main_page):
        main_page.click_constructor()
        assert "stellarburgers" in main_page.driver.current_url

    @allure.story("Переход на Ленту заказов")
    def test_click_order_feed(self, main_page):
        main_page.click_order_feed()
        assert "/feed" in main_page.driver.current_url
        feed_page = OrderFeedPage(main_page.driver)
        total = feed_page.get_total_counter_value()
        assert total >= 0