import pytest
import allure
from pages.duckduckgo_search_page import DuckDuckGoSearchPage

@allure.feature("DuckDuckGo Search")
@allure.story("Kullanıcı arama yapabilmeli")
@pytest.mark.parametrize("search_term", [
    "pytest",
    "selenium",
    "webdriver-manager",
])
def test_duckduckgo_search(driver, search_term):
    page = DuckDuckGoSearchPage(driver)
    with allure.step("Sayfayı yükle"):
        page.load()
    with allure.step(f"'{search_term}' terimini ara"):
        page.search(search_term)
    with allure.step("Sonucu doğrula"):
        assert search_term.lower() in driver.page_source.lower()
