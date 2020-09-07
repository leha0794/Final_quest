from .base_page import BasePage
from selenium import webdriver


class Do_It(BasePage):
    def Test_herest(self):
         self.driver = webdriver.Chrome()
         self.driver.find_element("btn-add-to-basket").click()
