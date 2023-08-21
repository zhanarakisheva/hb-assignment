from selenium.webdriver.common.by import By


# page_url = https://halykmarket.kz/favorite
class FavoritePage(object):
    def __init__(self, driver):
        self.driver = driver

    def product_cards(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "div.favorite-product div.product-card")
