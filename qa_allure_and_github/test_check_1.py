from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as WDW
import pytest
import time 
import allure #allure imported 


@pytest.fixture
@allure.title("Learning experiment on demoqa.com")
@allure.description("This test tests flaky test check,smoke testing, clicking of the described button below! ")
@allure.severity(allure.severity_level.NORMAL)
def setup():
    driver=webdriver.Chrome()
    yield driver 
    driver.quit()

@pytest.mark.flaky(reruns=2,reruns_delay=2) #useful for flaky test retry 2 times with 2 seconds delay
@pytest.mark.smoke #smoke testing (added it in pytest.ini before)
def test_crawl(setup): #function inherits something from setup function above
    driver=setup
    driver.get("https://demoqa.com/modal-dialogs")


    try:
        WDW(driver,10).until(ec.element_to_be_clickable((By.ID,"showLargeModal"))).click()
    except Exception as e:
        print("exception caught!!:",e)
        assert False,"something went wrong!"
    time.sleep(10)

    try:
        WDW(driver,5).until(ec.element_to_be_clickable((By.ID,"closeLargeModal"))).click()
    except Exception as e:
        print("exception caught!!:",e)
        assert False,"something went wrong!"
    time.sleep(2)
'''
@pytest.mark.flaky(reruns=2, reruns_delay=1) #retry logic test 
def test_example():
    assert 2+2==5  # This will fail and retry 2 times 
'''  
