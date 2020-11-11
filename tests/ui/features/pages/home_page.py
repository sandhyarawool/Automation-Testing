from antioch_ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    """
    Hudl Home Page
    """

    HOME_TAB = (By.CSS_SELECTOR, ".hui-globalnav__item > span")
    HOME_PAGE = (By.CSS_SELECTOR, ".uni-form__input")
    #QA_HIRE_PROJECT_TAB = (By.CSS_SELECTOR, ".hui-primaryteamswitcher__item:nth-child(1) > .hui-primaryteamswitcher__display-name")
    TEAMS_DROPDOWN = (By.CSS_SELECTOR, ".hui-primarynav__item--dropdown > span")
    SCHEDULE_TAB = (By.CSS_SELECTOR, ".hui-primarysubnav__item:nth-child(3) > span")
    
   
    def click_home_tab(self):
        return self.browser.wait.until_element_visible(*self.HOME_TAB).click() 

    def is_page_loaded(self):
        return self.browser.wait.until_element_visible(*self.HOME_PAGE)

    #def click_QA_Hire_Project_Tab(self):    
        #return self.browser.wait.until_element_visible(*self.QA_HIRE_PROJECT_TAB).click() 
    
    def click_Teams_Dropdown(self):    
        return self.browser.wait.until_element_visible(*self.TEAMS_DROPDOWN, time_out=30).click() 

    def click_Schedule_Tab(self):    
        return self.browser.wait.until_element_visible(*self.SCHEDULE_TAB).click() 
    
    

