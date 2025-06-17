
# Day-1 : Strated learning completed searching "django" keyword in "python.org" website , used : By(Name) ,webdriver function, then get used to extract website name,find_element,assertion use etc,.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome() #webdriver intialise

driver.get("https://www.python.org/") #going to access the website

print("page title:",driver.title) # Check the title
assert "Python" in driver.title 
time.sleep(2)

ele=driver.find_element(By.NAME,"q") #search box name is q
ele.clear()  
ele.send_keys("django") #key searching 
ele.send_keys(Keys.RETURN) #enter key auto

assert "Results" in driver.page_source
time.sleep(5)


driver.quit() #stop

# Day-2: Here automated login flow for a dummy website saucedemo.com and exceuted successfully, used By(ID)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

print("title:",driver.title) #title check
assert "Swag" in driver.title
time.sleep(3) #wiat 3 sec

driver.find_element(By.ID,"user-name").send_keys("problem_user") #username check
driver.find_element(By.ID,"password").send_keys("secret_sauce") #pwd check

driver.find_element(By.ID,"login-button").click() #button click

time.sleep(3)

driver.quit() #leave the browser

# Day-3: In this integrated error scenario using webdriverwait(alternate for time.sleep), used Xpath(tried id,contains) and learnt about using '*' in tag , and also used assertions and did print error message, and used try-catch-finally to ensure sucessful,unsucessful login and appropriate message for that, at last increased re-usablity of code by writing functions.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

def perfrom_login(driver,username,password):
    driver.get("https://www.saucedemo.com/")

    print("title:",driver.title) #title check
    assert "Swag" in driver.title

    WebDriverWait(driver,3).until(
        ec.presence_of_element_located((By.ID,"user-name"))
    ) # instead of time.sleep(3) we can use this 

    driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys(username) #username check
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys(password) #pwd check and 2nd way to write this //input[contains(@id,'pass')]

    driver.find_element(By.XPATH,"//input[@id='login-button']").click() #button click 2nd way to write this "//input[contains(@id,'login')]"
 
def check_error(driver):
    try:
        ele=WebDriverWait(driver,10).until(
            ec.visibility_of_element_located((By.XPATH,"//*[contains(text(),'Epic')]")) # if unsure about title use '*'
        )
        print("error message",ele.text)  #for printing errors

        assert "error" in ele.text, f"Expected 'error' in error message, but got: {ele.text}"
    except TimeoutException:
        print("Login suceesful!")

try:
    dv=webdriver.Chrome()
    perfrom_login(dv,"","secret_sauce")
    check_error(dv)
except Exception as e:
    print("test failed, ",e)
finally:
    dv.quit() #leave the browser

def test_py():
    assert 3*8==25 #day 5(checking pytest with multiple test cases)

def test_none():
    assert "Na" in "Naaani", "Fail"