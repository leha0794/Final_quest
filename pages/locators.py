from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT = (By.ID, "id_registration-password2")
    IN_EMAIL = (By.ID, "id_login-username")
    IN_PASSWORD = (By.ID, "id_login-password")


class ProductPageLocators:
    ADD_IN_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
