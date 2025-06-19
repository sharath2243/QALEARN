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
    
    def checkout(self):
        try:
            WDW(self.driver,4).until(ec.element_to_be_clickable((By.ID,"checkout"))).click()
            self.driver.find_element(*self.fname).send_keys("Lord")
            self.driver.find_element(*self.lname).send_keys("bhat")
            self.driver.find_element(*self.zip).send_keys("560091")

            self.driver.find_element(*self.cont).click() #continue button 

        except TimeoutException:
            return "something went wrong!!"

