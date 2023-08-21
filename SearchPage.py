from selenium.webdriver.common.by import By


# page_url = https://halykmarket.kz/search?r46_search_query=iPhone%2014%20Pro%20128%20Deep%20Purple&page=1
class SearchPage(object):
    def __init__(self, driver):
        self.driver = driver

    def search_result_header(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h1.category-page-title")

    def search_result_amount(self):
        return self.driver.find_element(By.CSS_SELECTOR, "span.category-page-amount")

    def product_cards(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "div.category-page-products div.product-card")
