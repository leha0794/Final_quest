from .base_page import BasePage
from .locators import BasePageLocators, ProductPageLocators, BasketPageLocators


class BasketPage(BasePage):
    def add_in_basket(self):
        self.click_element(*ProductPageLocators.ADD_IN_BASKET_NOT, "ADD_IN_BASKET_NOT")

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), "Not should be 'product' in basket"

    def should_be_text_in_basket_basketclear(self):
        self.expected_result_text(*BasketPageLocators.TEXT_FOR_CLEAR_BASKET,
                                  "TEXT_FOR_CLEAR_BASKET", "Your basket is empty. Continue shopping")

