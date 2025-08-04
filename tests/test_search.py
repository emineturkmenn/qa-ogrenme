import pytest
from pages.duckduckgo_search_page import DuckDuckGoSearchPage

@pytest.mark.parametrize("search_term", [
    "pytest",
    "selenium",
    "webdriver-manager",
])
def test_duckduckgo_search(driver, search_term):
    page = DuckDuckGoSearchPage(driver)
    page.load()
    page.search(search_term)
    assert search_term.lower() in driver.page_source.lower()
