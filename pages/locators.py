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
    NAME_PRODUCT = (By.XPATH, '//*[@class="product_page"]/div[@class="row"]/div[2]/h1')
    PRICE_PRODUCT = (By.XPATH, '//*[@class="price_color"]')
    NAME_PRODUCT_IN_ALERT = (By.CLASS_NAME, "alertinner")
    BUTTON_VIEW_BASKET = (By.XPATH, '//*[@class="basket-mini.pull-right.hidden-xs"]//*[@class="btn.btn-default"]')
    NAME_PRODUCT_IN_BASKET = (By.XPATH, '//div[@class="basket-items"]/div[@class="row"]/div[2]')
    PRICE_PRODUCT_IN_BASKET = (By.XPATH, '//div[@class="basket-items"]/div[@class="row"]/div[4]')

