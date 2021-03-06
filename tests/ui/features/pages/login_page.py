from antioch_ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    """
    Hudl Login Page
    """

    EMAIL_FIELD = (By.CSS_SELECTOR, "#email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#logIn")
    NEED_HELP_TAB = (By.CSS_SELECTOR, '#forgot-password-link')

    def enter_email(self, email):
        element = self.browser.wait.until_element_visible(*self.EMAIL_FIELD)
        element.click()
        element.send_keys(email)

    def enter_password(self, password):
        self.browser.wait.until_element_clickable(*self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.browser.wait.until_element_clickable(*self.LOGIN_BUTTON).click()

    def click_need_help_tab(self):
        self.browser.wait.until_element_clickable(*self.NEED_HELP_TAB).click()