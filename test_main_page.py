import pytest
import unittest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


class TestLoginFromMainPage:
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

