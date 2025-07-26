'''
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
'''
# options dropdown handle selenium.
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time #id:dropdown(option1,option2), class-name: form-control(10,20,50,etc,.), id : country
import pytest
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as ec
ts=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
import allure


@pytest.fixture(scope='function')
def setup():
    driver=webdriver.Chrome()
    driver.get("https://practice.expandtesting.com/dropdown")
    yield driver 
    driver.quit()

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.flaky(reruns=2,reruns_delay=2)
@allure.title("Random curiosity tries")
@allure.description("tested by- sharath Bhat")
@allure.step("dropdown check!")
def test_sel(setup):
    driver=setup
    try:
        dropdown_ele=WDW(driver,5).until(ec.visibility_of_element_located((By.ID,"dropdown")))
        dropdown=Select(dropdown_ele) #select must-do
        dropdown.select_by_value("1")
        assert dropdown.first_selected_option.get_attribute("value")=="1", "Wrong one, please verify!"
        print("SUCCESS")

    except Exception as e:
        print("exception caught!")
        driver.save_screenshot(f"dropdown_failure_{ts}.png")
        raise e
    time.sleep(3)

    try:
        dre1=driver.find_element(By.CLASS_NAME,"form-control")
        drop1=Select(dre1)
        drop1.select_by_index(2)
        assert drop1.first_selected_option.text=="50", "Wrong one, please verify!"
        print("2nd success!")
    except Exception as e:
        print("exception caught!")
        driver.save_screenshot(f"2nd_dropdown_failure_{ts}.png")
        raise e
    time.sleep(3)

    try:
        dre2=driver.find_element(By.XPATH,"//*[@id='country']")
        drop2=Select(dre2)
        drop2.select_by_visible_text("India")
        assert drop2.first_selected_option.text=="India", "Wrong one, please verify!"
        print("3rd success!")
    except Exception as e:
        print("exception caught!")
        driver.save_screenshot(f"3rd_dropdown_failure_{ts}.png")
        raise e
    time.sleep(3)

# alert,prompt handling using switch_to_alert
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time #id:dropdown(option1,option2), class-name: form-control(10,20,50,etc,.), id : country
import pytest
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as ec
ts=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

@pytest.fixture(scope='function')
def setup2():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    yield driver
    driver.quit() 

@pytest.mark.smoke
@pytest.mark.flaky(reruns=2,reruns_delay=2)
@allure.title("Random curiosity tries")
@allure.description("tested by- sharath Bhat")
@allure.step("alert,prompt checks!")
def test_func(setup2):
    driver=setup2
    try:
        WDW(driver,5).until(ec.element_to_be_clickable(driver.find_element(By.XPATH,"//button[contains(text(),'Alert')]"))).click() #alert it is!
        alert=driver.switch_to.alert #alert must-use 
        print("The alert text: ",alert.text) 
        time.sleep(3)
        alert.accept() #for ok use alert.accept
        print("The after click alert is: ",driver.find_element(By.ID,"result").text) # we can't use direct .text here!

    except Exception as e:
        print("exception caught!")
        driver.save_screenshot(f"alert_failure_{ts}.png")
        raise e
    
    try:
        WDW(driver,5).until(ec.element_to_be_clickable(driver.find_element(By.XPATH,"//button[contains(text(),'Confirm')]"))).click() #confirm it is!
        conf=driver.switch_to.alert #alert must-use 
        print("The confirm text: ",conf.text)
        time.sleep(3)
        conf.dismiss() #cancel button 
        print("The after click confirm message is: ",driver.find_element(By.ID,"result").text)

    except Exception as e:
        print("exception caught!")
        driver.save_screenshot(f"confirm_failure_{ts}.png")
        raise e
    
    try:
        WDW(driver,5).until(ec.element_to_be_clickable(driver.find_element(By.XPATH,"//button[contains(text(),'Prompt')]"))).click() #confirm it is!
        promp=driver.switch_to.alert #alert must-use (for anything alerts,prompts, or even confirmation popups)
        promp.send_keys("HI! I'm OPTIMUS PRIME😎")
        print("The prompt text : ",promp.text)
        time.sleep(3)
        promp.accept()
        print("The entered prompt message is: ",driver.find_element(By.ID,"result").text)

    except Exception as e:
        print("exception caught!")
        driver.save_screenshot(f"prompt_failure_{ts}.png")
        raise e
    time.sleep(3)
    


# fileinput (26th july)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import pytest
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait as WDW 
from selenium.webdriver.support import expected_conditions as ec
ts=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


@pytest.fixture(scope='function')
def setup3():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/upload") 
    yield driver
    driver.quit() 

@pytest.mark.smoke
@pytest.mark.flaky(reruns=2,reruns_delay=2)
@allure.title("Random curiosity tries")
@allure.description("tested by- sharath Bhat")
@allure.step("file input try!")
def test_drop(setup3):
    driver=setup3

    #ad overcome logic
    driver.execute_script("""
        ads=document.querySelectorAll(".ads,.googleads,iframe");
        ads.forEach(ad=>ad.style.display="none");
        console.log("Ads skipped✅");
""")
    
    try:
        filep=WDW(driver,5).until(ec.visibility_of_element_located((By.ID,"file-upload")))
        filep.send_keys(r"D:\test_journey\smart_cctv.txt")
        time.sleep(4)
        WDW(driver,5).until(ec.element_to_be_clickable((By.ID,"file-submit"))).click()
        time.sleep(2)
        res=WDW(driver,5).until(ec.visibility_of_element_located((By.TAG_NAME,"h3")))
        assert res.text=="File Uploaded!","❌Failed upload"

    except Exception as e:
        print("exception caught!",e)
        driver.save_screenshot(f"fileupload_failure_{ts}.png")
        raise e
