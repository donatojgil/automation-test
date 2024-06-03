from helpers.search_helper import SearchHelper
from helpers.home_helper import HomeHelper
from helpers.webdriver_helper import WebDriverHelper


def test_ali():
    # Initialise and get driver
    driver_manager = WebDriverHelper()
    driver = driver_manager.get_driver()
    # Perform the test requirement calling respective helpers
    home_helper = HomeHelper(driver)
    home_helper.page_loader()
    search_helper = SearchHelper(driver)
    search_helper.search("instax mini")
    search_helper.verify_results()
    # Quit driver
    driver.quit()
