from .locators import LoginPageLocators as LPL

from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_form(self):
        assert self.is_present(*LPL.LOGIN_FORM), f"Element woth selector {LPL.LOGIN_FORM} do not exist"
        
        
    def should_be_login_mail(self):
        assert self.is_present(*LPL.LOGIN_MAIL), f"Element woth selector {LPL.LOGIN_MAIL} do not exist"
        
    def should_be_login_pass(self):
        assert self.is_present(*LPL.LOGIN_PASS), f"Element woth selector {LPL.LOGIN_PASS} do not exist"

    def should_be_login_submit_btn(self):
        assert self.is_present(*LPL.LOGIN_BTN), f"Element woth selector {LPL.LOGIN_BTN} do not exist"
        
    def should_be_register_form(self):
        assert self.is_present(*LPL.REGISTER_FORM), f"Element woth selector {LPL.REGISTER_FORM} do not exist"
        
    def should_be_register_mail(self):
        assert self.is_present(*LPL.REGISTER_MAIL), f"Element woth selector {LPL.REGISTER_MAIL} do not exist"
        
    def should_be_register_pass(self):
        assert self.is_present(*LPL.REGISTER_PASS), f"Element woth selector {LPL.REGISTER_PASS} do not exist"
    
    def should_be_register_pass2(self):
        assert self.is_present(*LPL.REGISTER_PASS2), f"Element woth selector {LPL.REGISTER_PASS2} do not exist"

    def should_be_register_submit_btn(self):
        assert self.is_present(*LPL.REGISTER_BTN), f"Element woth selector {LPL.REGISTER_BTN} do not exist"
        
    def send_email(self):
        mail = self.browser.find_element(*LPL.LOGIN_MAIL)
        mail.send_keys("shurik51frolov@gmail.com")
        
    def send_pass(self):
        mail = self.browser.find_element(*LPL.LOGIN_PASS)
        mail.send_keys("Mupalu11157!")