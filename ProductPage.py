from selenium.webdriver.common.by import By


# page_url = https://halykmarket.kz/category/smartfoni/smartfon-apple-iphone-14-pro?sku=128gb_deep-purple&recommended_by=full_search&recommended_code=iphone%2014%20pro%20128%20deep%20purple
class ProductPage(object):
    def __init__(self, driver):
        self.driver = driver

    def product_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h1.desc-name")

    def favorite_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button.product-buttons-favorite")

    def favorites_page_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.icon-wrap")

    def price_value(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.desc-price-value")
