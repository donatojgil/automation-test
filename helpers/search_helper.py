from page_objects.search_page import SearchPage


class SearchHelper:

    def __init__(self, browser):
        self.browser = browser
        self.search_page = SearchPage(self.browser)

    def search(self, search_term):
        self.search_page.open(search_term)

    def verify_results(self):
        return self.search_page.validate_results()