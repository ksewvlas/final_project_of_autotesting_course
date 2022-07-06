from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "header span.btn-group a.btn-default")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, '#login_form a')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name="login_submit"]')

    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_CONFIRMATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ITEM_TITLE = (By.CSS_SELECTOR, '#content_inner h1')
    ITEM_PRICE = (By.CSS_SELECTOR, '#content_inner div.product_main p.price_color')
    MESSAGE_ITEM_TITLE = (By.CSS_SELECTOR, '#messages div.alert-success div.alertinner strong')
    MESSAGE_ITEM_PRICE = (By.CSS_SELECTOR, '#messages div.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div.alert-success')


class BasketPageLocators:
    BASKET_DIR = (By.CSS_SELECTOR, 'ul.breadcrumb li.active')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p > a')
    BASKET_ITEMS = (By.CSS_SELECTOR, '#content_inner div.basket-items')
