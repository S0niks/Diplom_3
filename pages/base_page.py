import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Поиск элемента по локатору: {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Поиск всех элементов по локатору: {locator}")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Клик по элементу: {locator}")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Получение текста элемента: {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание невидимости элемента: {locator}")
    def wait_for_element_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Выполнение JavaScript скрипта")
    def execute_script(self, script, *args):
        """Выполняет JavaScript на странице."""
        return self.driver.execute_script(script, *args)

    @allure.step("Ожидание выполнения условия")
    def wait_until(self, condition, timeout=10, message=""):
        """Ожидает, пока condition вернёт True (для кастомных ожиданий)"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(condition, message=message)