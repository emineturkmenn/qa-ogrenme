from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

driver_path = "C:\\Users\\Emine\\Desktop\\qa-ogrenme\\chromedriver-win64\\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://duckduckgo.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("selenium python")
search_box.send_keys(Keys.RETURN)

time.sleep(2)  

assert "selenium" in driver.page_source.lower()
print("Test passed!")

driver.quit()
