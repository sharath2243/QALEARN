from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as ec
import time

class Checkout_pom: #day-8: checkout pom
    def __init__(self,driver):
        self.driver=driver 
        self.fname=(By.ID,"first-name")
        self.lname=(By.ID,"last-name")
        self.zip=(By.ID,"postal-code")
        self.cont=(By.ID,"continue")
        self.finsih=(By.ID,"finish")
        self.canc=(By.ID,"cancel")
    
    def checkout(self):
        try:
            WDW(self.driver,4).until(ec.element_to_be_clickable((By.ID,"checkout"))).click()
            self.driver.find_element(*self.fname).send_keys("Lord")
            self.driver.find_element(*self.lname).send_keys("bhat")
            self.driver.find_element(*self.zip).send_keys("560091")

            self.driver.find_element(*self.cont).click() #continue button 
            

        except TimeoutException:
            return "something went wrong!!"
        
    def summary_check(self): #day-9: summary check and finish
        try:
            self.driver.find_element(*self.finsih).click() # finsish summary 
            time.sleep(4)
            WDW(self.driver,4).until(ec.element_to_be_clickable((By.ID,"back-to-products"))).click() #go back home
             
        except TimeoutException:
            return "something went wrong!!"
        
    def go_to_home(self): #day-9: cancel on checkout-page and go back to shop
        try:
            self.driver.find_element(*self.canc).click()
        except TimeoutException:
            return "something went wrong!!"