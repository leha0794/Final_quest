import math
from .locators import BasePageLocators
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def click_button_view_basket(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_VIEW_BASKET), "BUTTON_VIEW_BASKET not found"
        self.browser.find_element(*BasePageLocators.BUTTON_VIEW_BASKET).click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

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

    # Для себя универсальные функции
    def click_element(self, how, what, error_name):
        assert self.is_element_present(how, what), f"{error_name} not found"
        self.browser.find_element(how, what).click()

    def copy_text_element(self, how, what, error_name):
        assert self.is_element_present(how, what), f"{error_name} not found"
        text = self.browser.find_element(how, what).text
        return text

    def expected_result_text(self, how, what, error_name, expected_result):
        assert self.is_element_present(how, what), f"{error_name} not found"
        actual_result = self.browser.find_element(how, what).text
        assert actual_result == expected_result, f"{error_name}, \n actual result = {actual_result}, \n expected result = {expected_result}"

    def click_and_input_element(self, how, what, error_name, input_text):
        assert self.is_element_present(how, what), f"{error_name} not found"
        element = self.browser.find_element(how, what).click()
        element.send_keys(input_text)

    def input_element(self, how, what, error_name, input_text):
        assert self.is_element_present(how, what), f"{error_name} not found"
        self.browser.find_element(how, what).send_keys(input_text)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

