from .base_page import BasePage

import math
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_url_basket()
        self.should_be_add_in_basket()
        self.solve_quiz_and_get_code()

    def should_be_url_basket(self):
        pass

    def should_be_add_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_IN_BASKET), "Button ADD_IN_BASKET not found"
        self.browser.find_element(*ProductPageLocators.ADD_IN_BASKET).click()
        self.solve_quiz_and_get_code()

    def should_be_name_product_in_alert(self):
        Name_Product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        print(Name_Product)

    def go_to_basket(self):
        pass

    def should_be_name_product_in_basket(self):
        pass

    def should_be_price_in_basket(self):
        pass
