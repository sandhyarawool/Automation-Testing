from antioch_ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SchedulePage(BasePage):
    """
    Hudl Schedule Page
    """

    SEASONS = (By.CSS_SELECTOR, ".schedule-seasons")

    def is_page_loaded(self):
        return self.browser.wait.until_element_visible(*self.SEASONS)
    