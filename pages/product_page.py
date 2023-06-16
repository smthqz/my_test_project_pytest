from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        name = book_name.text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        price = book_price.text
        cart_link = self.browser.find_element(*ProductPageLocators.CART_LINK)
        cart_link.click()

    def should_be_the_same_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        addded_book_name = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_NAME)
        name = book_name.text
        added_book = addded_book_name.text
        assert name == added_book, 'Not the same name'

    def should_be_the_same_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        added_book_price = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_PRICE)
        price = book_price.text
        added_book = added_book_price.text
        assert price == added_book, 'Not the same price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is should be disappeared, but is presented'

