from .base_page import BasePage
from .locators import ProdactPageLocators as PPL
from selenium.webdriver.common.by import By

class ProdactPage(BasePage):
    
    def should_be_add_to_basket(self):
        assert self.is_present(*PPL.ADD_TO_BASKET), f"Element woth selector {PPL.ADD_TO_BASKET} do not exist"
    
    def click_add_to_basket(self):
        self.should_be_add_to_basket()
        btn = self.browser.find_element(*PPL.ADD_TO_BASKET)
        btn.click()
        
    def should_be_confirm_message(self):
        title = self.browser.find_element(*PPL.PRODUCT_MAIN).find_element(By.TAG_NAME, "h1").text
        message = self.browser.find_element(*PPL.MESSAGE).text

        assert title in message and "has been added to your basket." in message, "Incorrect message"
        
