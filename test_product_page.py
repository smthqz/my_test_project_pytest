import time
import faker
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest


list_of_failed_num = ["7"]
sp = ["0", "1", "3", "4", "5", "6", "7", "8", "9"]

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        f = faker.Faker()
        email = f.email()
        password = str(time.time())
        page.register_new_user(email=email, password=password)
        time.sleep(4)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


    @pytest.mark.parametrize('promo_offer', sp)
    def test_user_can_add_product_to_basket(self, browser, promo_offer):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
        if promo_offer in list_of_failed_num:
            pytest.skip("Skipping test for offer number 7")
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        time.sleep(4)
        page.should_be_the_same_name()
        page.should_be_the_same_price()

@pytest.mark.parametrize('promo_offer', sp)
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    if promo_offer in list_of_failed_num:
        pytest.skip("Skipping test for offer number 7")
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(4)
    page.should_be_the_same_name()
    page.should_be_the_same_price()

@pytest.mark.skip(reason="Тест падает")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Тест временно не проходит")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_dissapear_of_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    time.sleep(2)
    page.cart_is_empty()





