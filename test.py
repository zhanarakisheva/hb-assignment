#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from FavoritePage import FavoritePage
from HomePage import HomePage
from ProductPage import ProductPage
from SearchPage import SearchPage


class TestWebsite:
    # 1. Check browser configuration in browser_setup_and_teardown
    # 2. Run 'Selenium Tests' configuration
    # 3. Test report will be created in reports/ directory

    @pytest.fixture(autouse=True)
    def browser_setup_and_teardown(self):
        self.browser = webdriver.Chrome()

        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        self.browser.get("https://www.halykmarket.kz/")

        self.home_page = HomePage(self.browser)
        self.search_page = SearchPage(self.browser)
        self.product_page = ProductPage(self.browser)
        self.favorite_page = FavoritePage(self.browser)

        yield

        self.browser.close()
        self.browser.quit()


    def test_title(self):
        assert self.browser.title == "Halyk Market - Выгодные покупки в рассрочку"

    def test_search_input(self):
        self.home_page.search_input().send_keys("iPhone 14 Pro 128 Deep Purple")
        self.home_page.search_input().send_keys(Keys.ENTER)
        time.sleep(1)
        assert self.search_page.product_cards()

        search_product_card = None
        for product_card in self.search_page.product_cards():
            product_card_title = product_card.find_element(By.CSS_SELECTOR, "div.product-card-title").text
            if product_card_title == "Смартфон Apple iPhone 14 Pro 128Gb Deep Purple":
                search_product_card = product_card
                break
        assert search_product_card is not None

        search_product_price = search_product_card.find_element(By.CSS_SELECTOR, "span.product-card-value-value").text

        search_product_card.click()
        time.sleep(2)
        assert self.product_page.product_name().text == "Смартфон Apple iPhone 14 Pro 128Gb Deep Purple"

        self.product_page.favorite_button().click()
        time.sleep(2)

        self.product_page.favorites_page_button().click()
        time.sleep(2)
        favorite_product_card = None
        for favorite_product_card in self.favorite_page.product_cards():
            favorite_product_card_title = favorite_product_card.find_element(By.CSS_SELECTOR, "div.product-card-title").text
            if favorite_product_card_title == "Смартфон Apple iPhone 14 Pro 128Gb Deep Purple":
                favorite_product_card = favorite_product_card
                break
        assert favorite_product_card is not None

        favorite_product_price = favorite_product_card.find_element(By.CSS_SELECTOR, "span.product-card-value-value").text

        favorite_product_card.click()
        time.sleep(2)
        product_price = self.product_page.price_value().text
        assert search_product_price == favorite_product_price == product_price[3:]
