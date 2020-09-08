from .base_page import BasePage

import math
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.add_in_basket()
        self.should_be_add_in_basket()

    def add_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_IN_BASKET), "Button ADD_IN_BASKET not found"
        self.browser.find_element(*ProductPageLocators.ADD_IN_BASKET).click()
        self.solve_quiz_and_get_code()

    def should_be_add_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), "NAME_PRODUCT not found"
        Name_Product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), "PRICE_PRODUCT not found"
        Price_Product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT_IN_ALERT), "NAME_PRODUCT_IN_ALERT not found"
        Name_Product_In_Alert = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_ALERT).text
        assert Name_Product == Name_Product_In_Alert, f"In alert not is NAME this product, \n actual result = {Name_Product_In_Alert}, \n expected result = {Name_Product}"
        assert self.is_element_present(*ProductPageLocators.BUTTON_VIEW_BASKET), "BUTTON_VIEW_BASKET not found"
        self.browser.find_element(*ProductPageLocators.BUTTON_VIEW_BASKET).click()
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT_IN_BASKET), "NAME_PRODUCT_IN_BASKET not found"
        Name_Product_In_Basket = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_BASKET).text
        assert Name_Product == Name_Product_In_Basket, f"In basket not is NAME this product, \n actual result = {Name_Product_In_Basket}, \n expected result = {Name_Product}"
        Price_Product_In_Basket = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_BASKET).text
        assert Price_Product == Price_Product_In_Basket, f"In basket not is PRICE this product, \n actual result = {Price_Product_In_Basket}, \n expected result = {Price_Product}"


