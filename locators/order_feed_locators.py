from selenium.webdriver.common.by import By

class OrderFeedLocators:
    # TOTAL_COUNTER = (By.XPATH, "//p[contains(text(),'Выполнено за всё время')]/following-sibling::p")
    # TODAY_COUNTER = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p")
    
    TOTAL_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number__')]")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number__')]")
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady__')]/li")