#Day-4: learnt about POM(page object model)and seprate file structure for testing, imported csv too, then Created 2 files(one for POM,one for testing),wrote load,login,error functions in POM then wrote test_cases and imported login_pom from POM class then checked for any assertionerrors, and exceptions(webdriverExceptions,TImeoutExceptions) then gracefully quit the website(try-catch-finally).
from selenium import webdriver
from selenium.common.exceptions import WebDriverException,TimeoutException
from login_pom import Login_pom
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

def read_data(): # function for reading the data
    filepath = os.path.join(os.path.dirname(__file__),"login_details.csv")
    with open(filepath,newline='') as csvfile:
        reader=list(csv.DictReader(csvfile)) # reading data from csv
        return reader 
    
@pytest.mark.parametrize("test", read_data())
def test_data(test):
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

    time.sleep(2)
    driver.quit()