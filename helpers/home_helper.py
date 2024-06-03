from page_objects.home_page  import HomePage


class HomeHelper:

    def __init__(self, browser):
        self.browser = browser
        self.home_page = HomePage(self.browser)

    def page_loader(self):
        self.home_page.enter_page()
