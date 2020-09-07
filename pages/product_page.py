from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
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

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

