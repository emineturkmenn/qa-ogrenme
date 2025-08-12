import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def browser():
    options = ChromeOptions()
    options.add_argument("--headless=new")  # Headless mod, GitHub Actions için
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")  # Önemli, sandbox engelleri için
    options.add_argument("--disable-dev-shm-usage")  # Paylaşılan bellek sorunları için
    options.add_argument("--disable-gpu")  # GPU kullanımı devre dışı
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.wait = WebDriverWait(driver, 20)  # Maksimum 20 saniye bekle
    yield driver
    driver.quit()
