from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators
from .main_page import MainPage


class LoginPage(MainPage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Not login page'

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), 'No login form'

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), 'No register form'

    def register_new_user(self, email, password):
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        self.email = email
        self.password = password
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input2 = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT2)
        email_input.send_keys(email)
        password_input.send_keys(password)
        password_input2.send_keys(password)
        register_button.click()


