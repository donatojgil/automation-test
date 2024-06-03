import webdriver_manager.chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class WebDriverHelper:

    @staticmethod
    def get_driver():
        """
        Generates a new driver for Chrome using webdriver manager service and sets  basic options
        """
        # Create a new Chrome session
        service = Service(webdriver_manager.chrome.ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        driver.set_page_load_timeout(180)
        driver.maximize_window()
        driver.delete_all_cookies()
        return driver
