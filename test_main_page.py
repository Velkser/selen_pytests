import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.prodact_page import ProdactPage

@pytest.mark.main_page
class TestMainPageGuest:
    def test_guest_can_go_to_login_link_on_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link, 5)
        page.open()
        page.should_be_login_page()
        page.go_to_login_page()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProdactPage(browser, link)
        page.open()
        page.should_be_login_page()
        page.go_to_login_page()
    
def test_guest_can_use_login_form_on_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    page.should_be_login_mail()
    page.should_be_login_pass()
    page.should_be_login_submit_btn()
    


def test_guest_can_use_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
    page.should_be_register_mail()
    page.should_be_register_pass()
    page.should_be_register_pass2()
    page.should_be_register_submit_btn()



@pytest.mark.parametrize("book", [
                                    "hacking-exposed-wireless_208",
                                    "coders-at-work_207",
                                    pytest.param("visual-guide-to-lock-picking_206", marks=pytest.mark.xfail),
                                    "studyguide-for-counter-hack-reloaded_205",
                                    "gray-hat-hacking_204",
                                    "the-girl-who-played-with-non-fire_203",
                                    "reversing_202",
                                  ])
def test_guest_can_use_add_btn(browser, book):
    link = f"http://selenium1py.pythonanywhere.com/en-gb/catalogue/{book}/"
    page = ProdactPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.click_add_to_basket()
    page.should_be_confirm_message()
    



@pytest.mark.main_page
class TestMainPageUser:
    
    @pytest.fixture(scope = "function", autouse=True)
    def setup(self, browser):
        page = LoginPage(self, browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
        page.send_email()
        page.send_pass()
    
    def test_user_can_go_to_login_link_on_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link, 5)
        page.open()
        page.should_be_login_page()
        page.go_to_login_page()

    def test_user_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProdactPage(browser, link)
        page.open()
        page.should_be_login_page()
        page.go_to_login_page()