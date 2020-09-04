from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    x = LoginPage(browser, link)

    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    x.should_be_register_form()
    x.should_be_login_form()
    x.should_be_login_url()
