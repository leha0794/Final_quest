import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        login_page = LoginPage(browser, browser.current_url)

        page.open()
        page.go_to_login_page()
        page.should_be_login_link()
        login_page.should_be_register_form()
        login_page.should_be_login_form()
        login_page.should_be_login_url()


@pytest.mark.see_product_in_basket
class TestNotSeeProductInBasket():
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = BasketPage(browser, link)
        page.open()
        page.click_button_view_basket()
        page.should_not_be_product_in_basket()
        page.should_be_text_in_basket_basketclear()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasketPage(browser, link)
        page.open()
        page.click_button_view_basket()
        page.should_not_be_product_in_basket()
        page.should_be_text_in_basket_basketclear()
