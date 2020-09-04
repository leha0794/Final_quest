from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "В URl нет строки login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.IN_EMAIL), "'LOG IN' Field for email not found"
        assert self.is_element_present(*LoginPageLocators.IN_PASSWORD), "'LOG IN' Field for password not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "'REGISTRATION' Field for email not found"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), "'REGISTRATION' Field for password not found"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT), "'REGISTRATION' Field for password repeat not found"
