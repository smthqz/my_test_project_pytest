from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, '[name="registration-email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[name="registration-password1"]')
    PASSWORD_INPUT2 = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form > button')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')

class ProductPageLocators:
    CART_LINK = (By.CSS_SELECTOR, '[value="Добавить в корзину"]')
    ADDED_BOOK_NAME = (By.CSS_SELECTOR, '#messages strong')
    ADDED_BOOK_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, '[href="/ru/basket/"]')
    EMPTY_CART = (By.CSS_SELECTOR, 'div .content p')




