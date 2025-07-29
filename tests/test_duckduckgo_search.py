from pages.duckduckgo_search_page import DuckDuckGoSearchPage

def test_duckduckgo_search(driver):
    duckduckgo = DuckDuckGoSearchPage(driver)
    duckduckgo.load()
    duckduckgo.search("selenium python")
    
    assert "selenium python" in driver.page_source.lower()