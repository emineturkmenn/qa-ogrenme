from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DuckDuckGoResultPage:
    RESULT_LINKS = (By.CSS_SELECTOR, "a[data-testid='result-title-a']")

    def __init__(self, driver):
        self.driver = driver

    def wait_for_results(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.RESULT_LINKS)
        )

    def result_links_count(self):
        return len(self.driver.find_elements(*self.RESULT_LINKS))

    def get_first_result_link(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="result-title-a"]'))
        )