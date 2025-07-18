#Day-4: learnt about POM(page object model)and seprate file structure for testing, imported csv too, then Created 2 files(one for POM,one for testing),wrote load,login,error functions in POM then wrote test_cases and imported login_pom from POM class then checked for any assertionerrors, and exceptions(webdriverExceptions,TImeoutExceptions) then gracefully quit the website(try-catch-finally).
from selenium import webdriver
from selenium.common.exceptions import WebDriverException,TimeoutException
from POM.login_pom import Login_pom
from POM.product_pom import Product_pom
from POM.checkout_pom import Checkout_pom
import time 
import csv
import pytest
import os
from datetime import datetime
ts=datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
import allure

'''
def read_data(file_path):
    with open(file_path,newline='') as csvfile: #reading from an external csv file (whic is doing the same job as wrtitng in a list of dictionary records)
        return list(csv.DictReader(csvfile))

test_cases=read_data("login_details.csv")

for test in test_cases:
    try:
        driver=webdriver.Chrome() #intialised web driver 
        login=Login_pom(driver) #created a class object
        login.load() # calling load function,loading website 
        login.login(test["user"].strip(),test["pwd"].strip()) #calling login function, with username and password parameters(used strip because of parsing issue)
        err=login.error_mes() #any error?, error function call 

        if test["expected"]=="fail": #used assertions for double check nd printing error or no error
            assert err is not None,"expected errors, but unexpected happenend!"
            print(f"[❌ FAIL as expected] Error message: {err}")
        else:
            assert err is None, "no errors still login not sucessful!"
            print(f"[✅ PASS] Login successful!")

    except (WebDriverException,TimeoutException) as e: #any exceptions 
        print("Exception caught:",e)
    
    finally:
        driver.quit() #quit
        time.sleep(2)
'''

#day-5: above same thing but with using pytest(without for loop and try catch finally)

@pytest.fixture #day-6: using pytest.fixture for recurring setup-teardown
def setup():
    options = webdriver.ChromeOptions()
    
    # ✅ Enable headless only in GitHub Actions
    if os.getenv("GITHUB_ACTIONS") == "true":
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def read_login_data(): # function for reading the login data
    filepath = os.path.join(os.path.dirname(__file__),"..","Csv_files","login_details.csv")
    with open(filepath,newline='') as csvfile:
        reader=list(csv.DictReader(csvfile)) # reading data from csv
        return reader 
    
def read_add_prod(): #day-7:function to reading the add product data
    filepath=os.path.join(os.path.dirname(__file__),"..","Csv_files","add_product.csv")
    with open(filepath,newline='') as csvfile:
        reader=list(csv.DictReader(csvfile))
        return reader

def read_remove_prod(): #day-8:function to reading the remove product data
    filepath=os.path.join(os.path.dirname(__file__),"..","Csv_files","remove_product.csv")
    with open(filepath,newline='') as csvfile:
        reader=list(csv.DictReader(csvfile))
        return reader
    
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("test", read_login_data()) 
@allure.title("Selenium automation on saucedemo.com")
@allure.description("Tested By: Sharath R Bhat")
@allure.severity(allure.severity_level.NORMAL)
def test_data(setup,test):

    driver=setup #using pytest.fixture setup

    login=Login_pom(driver) #created a class object
    login.load() # calling load function,loading website 
    login.login(test["user"].strip(),test["pwd"].strip()) #calling login function, with username and password parameters(used strip because of parsing issue)
    err=login.error_mes() #any error?, error function call 

    if test["expected"]=="fail": #used assertions for double check nd printing error or no error
        assert err is not None,"expected errors, but unexpected happenend!"
        print(f"[❌ FAIL as expected] Error message: {err}")
       

    else:
        assert err is None, "no errors still login not sucessful!"
        print(f"[✅ PASS] Login successful!")
       

        product=Product_pom(driver) #created a class object
        time.sleep(4)

        product.poduct_title() #only for 1 i have checked.
        print("[✅ PASS] Title check,description check!")

        try:
            for item in read_add_prod(): #day-7:iterating through csv read function
                time.sleep(2) 
                res=product.add_product(item["product_id"]) #adding each product
                assert res is None,res
            print("[✅ PASS] Product added successfuly!")

        except Exception as e:
            driver.save_screenshot(f"Screenshots/{item['product_id']}_{ts}.png") #day-8: introduced save screenshots if any error
            raise e

        try:
            for item in read_remove_prod(): #day-8: iterating through csv read function
                time.sleep(2)
                res=product.remove_product(item["product_id"])
                assert res is None,res
            print("[✅ PASS] Products removed successfuly!")

        except Exception as e:
            driver.save_screenshot(f"Screenshots/{item['product_id']}_{ts}.png")
            raise e


        time.sleep(4) #day-7: knowingly including delays..

        product.add_product("add-to-cart-sauce-labs-bolt-t-shirt") #day-8:after removing everything 1 item i added just to ensure not empty cart
        
        try:
            product.go_to_cart()
            time.sleep(3) #day-9: 3 seconds delay
            product.go_back() #go back to shopping page
            time.sleep(2) # wait for 2 seconds
            product.go_to_cart() # go to cart again

            print("[✅ PASS] GO-TO-CART checkup done!")
        except Exception as e:
            driver.save_screenshot(f"Screenshots/go_to_cart_f_{ts}.png") 
            raise e

        checkout=Checkout_pom(driver) #checkout driver intialisation
        
        time.sleep(4)
        
        try: #day-8: checkout process
            checkout.checkout() #checkout call
            time.sleep(2)
            checkout.go_to_home() #DAy-9: canels and goes to home
            time.sleep(2)

            product.add_product("add-to-cart-sauce-labs-onesie") # then adds another product

            product.go_to_cart() #goes to cart
            time.sleep(2)

            checkout.checkout() #checksout
            time.sleep(2)

        except Exception as e:
            driver.save_screenshot(f"Screenshots/checkout_f_{ts}.png")
            raise e

        time.sleep(4)

        try: #day-9: summary check process
            checkout.summary_check() #summary check call
        
            print("[✅ PASS] CHECKOUT checkup done!")
        except Exception as e:
            driver.save_screenshot(f"Screenshots/summary_check_f_{ts}.png")
            raise e

        time.sleep(4)

        try:
            login.logout()
            print("[✅ PASS] logout successful!")
        except Exception as e:
            driver.save_screenshot(f"Screenshots/logout_f_{ts}.png")
            raise e
