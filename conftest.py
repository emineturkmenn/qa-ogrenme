import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def browser(request):
    options = ChromeOptions()

    headless = request.config.getoption("--headless") if hasattr(request.config, 'getoption') else False
    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1920,1080")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.wait = WebDriverWait(driver, 10)

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", default=False, help="Headless modda çalıştır"
    )
