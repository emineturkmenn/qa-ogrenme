import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", help="Headless modda çalıştır"
    )

@pytest.fixture
def browser():
    options = ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.wait = WebDriverWait(driver, 10)
    yield driver
    driver.quit()