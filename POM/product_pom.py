from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as ec

class Product_pom:
    def __init__(self,driver):
        self.driver=driver
        self.product_add_btn=(By.ID,"add-to-cart-sauce-labs-backpack")
        self.cart_icon=(By.CLASS_NAME,"shopping_cart_link")
    
    def add_product(self):
        try:
           ele=WDW(self.driver,2).until(ec.element_to_be_clickable((self.product_add_btn))).click()
        except TimeoutException:
            return "Something went wrong"
    def go_to_cart(self):
        try:
           ele=WDW(self.driver,2).until(ec.element_to_be_clickable((self.cart_icon))).click()
        except TimeoutException:
            return "failed"

