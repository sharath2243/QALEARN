#Day-4: learnt about POM(page object model)and seprate file structure for testing, imported csv too, then Created 2 files(one for POM,one for testing),wrote load,login,error functions in POM then wrote test_cases and imported login_pom from POM class then checked for any assertionerrors, and exceptions(webdriverExceptions,TImeoutExceptions) then gracefully quit the website(try-catch-finally).
from selenium import webdriver
from selenium.common.exceptions import WebDriverException,TimeoutException
from POM.login_pom import Login_pom
from POM.product_pom import Product_pom
import time 
import csv
import pytest
import os

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
    driver=webdriver.Chrome() #intialised webdriver here
    yield driver # to perform cleanup after tests are run (setup-teardown)
    driver.quit() #quit 

def read_login_data(): # function for reading the data
    filepath = os.path.join(os.path.dirname(__file__),"..","Csv_files","login_details.csv")
    with open(filepath,newline='') as csvfile:
        reader=list(csv.DictReader(csvfile)) # reading data from csv
        return reader 
    
def read_add_prod(): #day-7:function to reading the add product data
    filepath=os.path.join(os.path.dirname(__file__),"..","Csv_files","add_product.csv")
    with open(filepath,newline='') as csvfile:
        reader=list(csv.DictReader(csvfile))
        return reader
    

@pytest.mark.parametrize("test", read_login_data()) 
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
        
        product.poduct_title()

        for item in read_add_prod(): #day-7:iterating through csv read function
            time.sleep(2) 
            res=product.add_product(item["product_id"]) #adding each product
            assert res is None,res


        time.sleep(4) #day-7: knowingly including delays..
        product.go_to_cart()

        time.sleep(4)
        product.remove_product()

        time.sleep(4)
        login.logout()