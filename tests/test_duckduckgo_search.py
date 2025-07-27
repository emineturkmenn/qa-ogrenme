from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_duckduckgo_search_valid_query(driver):
    driver.get("https://duckduckgo.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("selenium python")
    search_box.submit()
    assert "selenium python" in driver.page_source.lower()

def test_duckduckgo_search_empty_query(driver):
    driver.get("https://duckduckgo.com/")
    search_box = driver.find_element("name", "q")
    search_box.send_keys("")
    search_box.submit()
    assert "results" not in driver.page_source.lower()
    