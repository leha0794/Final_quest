from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.add_in_basket()
        self.should_be_add_in_basket()

    def add_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_IN_BASKET), "Button ADD_IN_BASKET not found"
        self.browser.find_element(*ProductPageLocators.ADD_IN_BASKET).click()
        self.solve_quiz_and_get_code()

    def should_be_add_in_basket(self):
        Name_Product = self.copy_text_name_product()
        Price_Product = self.copy_text_price_product()
        Name_Product_In_Alert = self.copy_text_price_produc_in_alert()
        self.check_expected_result_for_name_to_alert(Name_Product, Name_Product_In_Alert)
        self.click_button_view_basket()
        Name_Product_In_Basket = self.copy_text_price_produc_in_basket()
        self.check_expected_result_for_name_to_basket(Name_Product, Name_Product_In_Basket)
        Price_Product_In_Basket = self.copy_text_price_product_in_basket()
        self.check_expected_result_for_price_to_basket(Price_Product, Price_Product_In_Basket)

    # ---------------------------------------------------------------------------------------------
    #  Это можно как-то поробовать обьединть
    def check_expected_result_for_price_to_basket(self, Price_Product, Price_Product_In_Basket):
        assert Price_Product == Price_Product_In_Basket, f"In basket not is PRICE this product, \n actual result = {Price_Product_In_Basket}, \n expected result = {Price_Product}"

    def check_expected_result_for_name_to_basket(self, Name_Product, Name_Product_In_Basket):
        assert Name_Product == Name_Product_In_Basket, f"In basket not is NAME this product, \n actual result = {Name_Product_In_Basket}, \n expected result = {Name_Product}"

    def check_expected_result_for_name_to_alert(self, Name_Product, Name_Product_In_Alert):
        assert Name_Product == Name_Product_In_Alert, f"In alert not is NAME this product, \n actual result = {Name_Product_In_Alert}, \n expected result = {Name_Product}"
    # ---------------------------------------------------------------------------------------------

    # ====================================================================================================================
    # Эти методы, нужно потом попытаться обьединить, и сделать новый в который я буду просто прокидывать переменную локатора
    # и дальше он сам найдет что нужно, сейчас я пишу отдельно метод для цены продукта и для имени
    def copy_text_price_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT_IN_BASKET), "PRICE_PRODUCT_IN_BASKET not found"
        Price_Product_In_Basket = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_BASKET).text
        return Price_Product_In_Basket

    def copy_text_price_produc_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT_IN_BASKET), "NAME_PRODUCT_IN_BASKET not found"
        Name_Product_In_Basket = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_BASKET).text
        return Name_Product_In_Basket

    def copy_text_price_produc_in_alert(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT_IN_ALERT), "NAME_PRODUCT_IN_ALERT not found"
        Name_Product_In_Alert = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_ALERT).text
        return Name_Product_In_Alert

    def copy_text_price_product(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), "PRICE_PRODUCT not found"
        Price_Product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        return Price_Product

    def copy_text_name_product(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), "NAME_PRODUCT not found"
        Name_Product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        return Name_Product
    # ====================================================================================================================

    def click_button_view_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_VIEW_BASKET), "BUTTON_VIEW_BASKET not found"
        self.browser.find_element(*ProductPageLocators.BUTTON_VIEW_BASKET).click()

    def should_not_be_success_message_alert(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_PRODUCT_IN_ALERT), \
            "Not should be 'alert' for product"

    def should_not_be_success_message_aler_after(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_PRODUCT_IN_ALERT), \
            "Should be closed 'alert' for product after 4 second"

