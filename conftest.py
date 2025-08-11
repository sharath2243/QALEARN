#conftest.py for common driver setup for ui testing ✅
import pytest 
from selenium import webdriver
import os 

@pytest.fixture(scope='session')
def setup2():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")

    if os.getenv("GITHUB_ACTIONS") == "true":
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit() 
