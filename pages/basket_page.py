from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def cart_is_empty(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_CART), 'Cart is not empty'

    def cart_is_not_empty(self):
        assert not self.browser.find_element(*BasketPageLocators.EMPTY_CART), 'Cart is empty'

