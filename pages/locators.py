from selenium.webdriver.common.by import By

class MainPageLocators:
    ...
    
class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SEARCH_LINK = (By.NAME, "q")  
    VIEW_BASCET = (By.CSS_SELECTOR, ".btn-group > a")
    
    
class ProdactPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_MAIN = (By.CSS_SELECTOR, ".product_main")
    MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_MAIL = (By.NAME, "login-username")
    LOGIN_PASS = (By.NAME, "login-password")
    LOGIN_BTN = (By.NAME, "login_submit")

    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_MAIL = (By.NAME, "registration-email")
    REGISTER_PASS = (By.NAME, "registration-password1")
    REGISTER_PASS2 = (By.NAME, "registration-password2")
    REGISTER_BTN = (By.NAME, "registration_submit")
    
    
