from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.duckduckgo_search_page import DuckDuckGoSearchPage

def test_duckduckgo_search_returns_results(driver):
    search_term = "selenium python"
    duckduckgo = DuckDuckGoSearchPage(driver)
    duckduckgo.load()
    duckduckgo.search(search_term)

    results_locator = (By.CSS_SELECTOR, "a[data-testid='result-title-a']")
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(results_locator)
    )

    assert results, "Arama sonucu bulunamadı."

    first_result_text = results[0].text.lower()
    assert any(term in first_result_text for term in search_term.split()), (
        f"İlk sonuç '{first_result_text}' arama terimini içermiyor."
    )
