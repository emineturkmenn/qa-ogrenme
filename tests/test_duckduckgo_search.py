from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.duckduckgo_search_page import DuckDuckGoSearchPage
from pages.duckduckgo_result_page import DuckDuckGoResultPage

def test_duckduckgo_search_returns_results(driver):
    search_term = "selenium python"
    duckduckgo = DuckDuckGoSearchPage(driver)
    duckduckgo.load()
    duckduckgo.search(search_term)

    results_locator = (By.CSS_SELECTOR, "a[data-testid='result-title-a']")
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(results_locator)
    )

    result_page = DuckDuckGoResultPage(driver)
    first_result = result_page.get_first_result_link()
    print(first_result.text.lower())

    first_result.click()