import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
import requests
from urls import BASE_URL, API_BASE
from data import INGREDIENT_NAME, INGREDIENT_NAME_FILLING
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.ingredient_modal import IngredientModal
from pages.order_modal import OrderModal
from pages.base_page import BasePage
import allure
import random
import string

def generate_user_data():
    email = ''.join(random.choices(string.ascii_lowercase, k=8)) + '@test.com'
    password = 'password123'
    name = ''.join(random.choices(string.ascii_lowercase, k=6)).capitalize()
    return email, password, name

@pytest.fixture(scope="function")
def registered_user():
    email, password, name = generate_user_data()
    payload = {"email": email, "password": password, "name": name}
    resp = requests.post(f"{API_BASE}/auth/register", json=payload)
    assert resp.status_code == 200, f"Не удалось создать пользователя: {resp.text}"
    data = resp.json()
    token = data.get("accessToken")
    yield {
        "email": email,
        "password": password,
        "name": name,
        "token": token
    }

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    browser_name = request.param
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError("Unsupported browser")
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(browser):
    return MainPage(browser)

@pytest.fixture
def order_feed_page(browser):
    return OrderFeedPage(browser)

@pytest.fixture
def ingredient_modal(browser):
    return IngredientModal(browser)

@pytest.fixture
def order_modal(browser):
    return OrderModal(browser)

@pytest.fixture
def logged_in_browser(browser, registered_user):
    driver = browser
    main = MainPage(driver)
    main.click_personal_account()
    base = BasePage(driver)
    # Ждём появления кнопки "Войти" (признак страницы логина)
    base.wait_for_element_visible((By.XPATH, "//button[text()='Войти']"))
    # Поле Email - ищем по лейблу
    email_input = base.find_element((By.XPATH, "//label[text()='Email']/following-sibling::input"))
    email_input.send_keys(registered_user["email"])
    # Поле Пароль - аналогично
    password_input = base.find_element((By.XPATH, "//label[text()='Пароль']/following-sibling::input"))
    password_input.send_keys(registered_user["password"])
    # Кнопка Войти
    base.find_element((By.XPATH, "//button[text()='Войти']")).click()
    # Ждём появления кнопки "Оформить заказ" на главной (после авторизации)
    base.wait_for_element_visible((By.XPATH, "//button[text()='Оформить заказ']"))
    yield driver