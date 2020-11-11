from antioch_ui import utils
from behave import given, when, then
import time

from features.pages.login_page import LoginPage
from features.pages.home_page import HomePage

# Givens


@given('I want to log in to Hudl as {}')
def go_to_login_page(context, user):
    context.user = utils.load_user_json(context, user)
    context.browser.load(context, 'login')


# Whens



@when('I log in')
def doLogin(context):
    """
    :param context: Behave context object
    Simple login with the context user and password
    """
    login_page = LoginPage(context.browser)

    login_page.enter_email(context.user['user'])
    login_page.enter_password(context.password)
    login_page.click_login_button()

use_step_matcher("re")

@when('I click on home Page')
def click_home_page(context):
    home_page = HomePage(context.browser)
    home_page.click_home_tab()


@then('I should be directed to my home page')
def check_landed_on_profile_page(context):
    home_page = HomePage(context.browser)
    assert home_page.is_page_loaded(), 'User not directed to home page after login'

    
