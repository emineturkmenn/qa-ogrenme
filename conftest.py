import pytest 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture
def driver():
    chrome_driver_path = os.path.join(os.getcwd(), "drivers", "chromedriver-win64", "chromedriver.exe")
    
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    
    yield driver
    driver.quit()