from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as WDW
import pytest
import time 
from datetime import datetime
import allure #allure imported 
ts=datetime.now().strftime("%y-%m-%d-%H-%M-%S")


@pytest.fixture
@allure.title("Learning experiment on demoqa.com")
@allure.description("This test tests flaky test check,smoke testing, without impleemnting re-run logic ")
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
        time.sleep(10)
        WDW(driver,5).until(ec.element_to_be_clickable((By.ID,"closeLargeModal"))).click()
    except Exception as e:
        print("exception caught!!:",e)
        filename=f"failure_screenshot_{ts}.png"
        driver.save_screenshot(filename)
        allure.attach.file(filename,name='Screenshots',attachment_type=allure.attachment_type.PNG)
        assert False,"something went wrong!"
    time.sleep(2)
'''
@pytest.mark.flaky(reruns=2, reruns_delay=1) #retry logic test 
def test_example():
    assert 2+2==5  # This will fail and retry 2 times 
'''  
