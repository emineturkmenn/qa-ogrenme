import pytest
import allure
from pages.duckduckgo_search_page import DuckDuckGoSearchPage

@allure.feature("DuckDuckGo Search")
@allure.story("Kullanıcı arama yapabilmeli")
@pytest.mark.parametrize("search_term", [
    "pytest",
    "selenium",
])
def test_duckduckgo_search(browser, search_term):
    page = DuckDuckGoSearchPage(browser)
    with allure.step("Sayfayı yükle"):
        page.load()
    with allure.step(f"'{search_term}' terimini ara"):
        page.search(search_term)
    with allure.step("Sonucu doğrula"):
        assert search_term.lower() in browser.page_source.lower()
