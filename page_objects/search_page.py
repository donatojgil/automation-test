from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class SearchPage:
    SEARCH = (By.ID, 'search-words')
    SUBMIT = (By.CLASS_NAME,'search--submit--2VTbd-T')
    RESULTS = (By.CSS_SELECTOR, '#card-list > div')

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 20)

    def open(self, search_term):
        self.browser.find_element(*self.SEARCH).send_keys(search_term)
        element = self.wait.until(ec.element_to_be_clickable(self.SUBMIT))
        element.click()

    def validate_results(self):
        try:
            self.wait.until(ec.visibility_of_element_located(self.RESULTS))
            return True
        except:
            return False



