from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as ec
import time

class Product_pom:
    def __init__(self,driver):
        self.driver=driver
        self.cart_icon=(By.CLASS_NAME,"shopping_cart_link")
       #self.product_add_btn=(By.ID,"add-to-cart-sauce-labs-bike-light")
       #self.product_remove_btn=(By.ID,"remove-sauce-labs-bike-light")
    
    ''' def add_product(self): #singl product add
        try:
           WDW(self.driver,4).until(ec.element_to_be_clickable((self.product_add_btn))).click()
        except TimeoutException:
            return "Something went wrong"

        def remove_product(self): #day-7:to remove a single product
        try:
            WDW(self.driver,4).until(ec.element_to_be_clickable((self.product_remove_btn))).click()
        except TimeoutException:
            return "Error!"
    '''

    def add_product(self,product_id): #day-7:multi product add by csv
        try:
            WDW(self.driver,4).until(ec.element_to_be_clickable((By.ID,product_id))).click()
        except TimeoutException:
            return "something went wrong!!"
        
    def go_to_cart(self): #day-6:go to cart
        try:
           WDW(self.driver,4).until(ec.element_to_be_clickable((self.cart_icon))).click()
        except TimeoutException:
            return "failed"
    
    def remove_product(self,product_id): #day-8:multi product remove by csv
        try:
            WDW(self.driver,4).until(ec.element_to_be_clickable((By.ID,product_id))).click()
        except TimeoutException:
            return "something went wrong!!"
        
        
    def poduct_title(self): #day-7: function to check title and come back button check
        try:
            WDW(self.driver,4).until(ec.element_to_be_clickable((By.ID,"item_4_title_link"))).click()
            time.sleep(4)
            WDW(self.driver,4).until(ec.element_to_be_clickable((By.ID,"back-to-products"))).click()
        except TimeoutException:
            return "Error!"
    
   