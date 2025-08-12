import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Tarayıcı adı: chrome"
    )
    parser.addoption(
        "--headless", action="store_true", help="Headless modda çalıştır"
    )

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        # --user-data-dir kullanılmıyor!
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    else:
        raise ValueError(f"Geçersiz tarayıcı seçimi: {browser_name}")

    driver.wait = WebDriverWait(driver, 10)
    yield driver
    driver.quit()
