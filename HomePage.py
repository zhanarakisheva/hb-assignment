from selenium.webdriver.common.by import By


# page_url = https://www.halykmarket.kz
class HomePage(object):
    def __init__(self, driver):
        self.driver = driver

    def search_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input.search-input")


