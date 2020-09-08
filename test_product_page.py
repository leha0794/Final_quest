from .pages.product_page import ProductPage
import pytest
from .pages.main_page import MainPage
import time


def test_guest_can_go_to_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)

    product_page.open()
    product_page.add_in_basket()
    product_page.should_be_add_in_basket()
    # time.sleep(999)




