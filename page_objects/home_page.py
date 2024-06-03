from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class HomePage:
    

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def enter_page(self):
        self.browser.get("https://aliexpress.com/")