
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as WDW
import pytest
import time 
import os
from datetime import datetime
import allure #allure imported 
ts=datetime.now().strftime("%y-%m-%d-%H-%M-%S")


@pytest.mark.flaky(reruns=4,reruns_delay=2) #useful for flaky test retry 2 times with 2 seconds delay
@pytest.mark.smoke #smoke testing (added it in pytest.ini before)
@pytest.mark.ui
@allure.title("Learning experiment on demoqa.com")
@allure.description("This test tests flaky test check,smoke testing, without impleemnting re-run logic by Sharath Bhat ")
@allure.severity(allure.severity_level.NORMAL)
def test_crawl(setup2): #function inherits something from setup function above
    driver=setup2
    driver.get("https://demoqa.com/modal-dialogs")
     
    #ad block logic (chatgpt gave me i wrote!)
    driver.execute_script("""
        let ads=document.querySelectorAll("iframe,.adsbygoogle,.ads");
        ads.forEach(ad=>ad.style.display="none");
        console.log("ads hidden");
    """)
    print("Ads skipped!✅")
    
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
