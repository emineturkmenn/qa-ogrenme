from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class DuckDuckGoSearchPage:
    URL = "https://duckduckgo.com/"
    SEARCH_INPUT = (By.ID, "searchbox_input")
    RESULT_LINKS = (By.CSS_SELECTOR, "a[data-testid='result-title-a']")  # Doğrulama için

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def search(self, phrase):
        search_input = self.driver.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        search_input.clear()
        search_input.send_keys(phrase + Keys.RETURN)

    def results_exist(self):
        return self.driver.wait.until(
            EC.presence_of_all_elements_located(self.RESULT_LINKS)
        )