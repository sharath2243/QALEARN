from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

class Login_pom:
    def __init__(self,driver): #constructor for intialisation of username,pws,driver,login-button,url
        self.url="https://www.saucedemo.com/"
        self.driver=driver 
        self.username=(By.ID,"user-name")
        self.password=(By.ID,"password")
        self.login_button=(By.ID,"login-button")
        self.error=(By.XPATH,"//*[contains(text(),'Epic')]")
    
    def load(self): #load function to load the website
        self.driver.get(self.url)
    
    def error_mes(self): #error hanndling function
        try:
            ele=WDW(self.driver,5).until(
                ec.visibility_of_element_located(self.error)
            )
            return f"error: {ele.text}"
        except TimeoutException:
            return None 
    
    def login(self,usr,pwd): #main login function which is running with the help of constructor
        WDW(self.driver,5).until(ec.visibility_of_element_located(self.username))
        self.driver.find_element(*self.username).send_keys(usr)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()