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
    NAME_PRODUCT_IN_ALERT = (By.XPATH, '//div[@class="alertinner "]//strong')
    BUTTON_VIEW_BASKET = (By.XPATH, '//*[@class="basket-mini pull-right hidden-xs"]//*[@class="btn btn-default"]')
    NAME_PRODUCT_IN_BASKET = (By.XPATH, '//div[@class="basket-items"]/div[@class="row"]/div[2]/h3')
    PRICE_PRODUCT_IN_BASKET = (By.XPATH, '//div[@class="basket-items"]/div[@class="row"]/div[4]')
    ADD_IN_BASKET_NOT = (By.XPATH, '//*[@class="basket-mini pull-right hidden-xs"]e//*[@class="btn btn-default"]')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_VIEW_BASKET = (By.XPATH, '//*[@class="basket-mini pull-right hidden-xs"]//*[@class="btn btn-default"]')


class BasketPageLocators:
    BASKET_FORMSET = (By.ID, "basket_formset")
    TEXT_FOR_CLEAR_BASKET = (By.ID, "content_inner")
    XXX = (By.CLASS_NAME, "page-header")

