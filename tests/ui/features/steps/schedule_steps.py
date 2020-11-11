from antioch_ui import utils
from behave import given, when, then
import time

from features.pages.login_page import LoginPage
from features.pages.home_page import HomePage
from features.pages.schedule_page import SchedulePage

@when('I click on Teams Dropdown')
def click_Teams_Dropdown(context):
    home_page = HomePage(context.browser)
    home_page.click_Teams_Dropdown()

@when('I click on Schedule Tab')
def click_Teams_schedule_tab(context):
    home_page = HomePage(context.browser)
    home_page.click_Schedule_Tab()


@when('I deep link to schedule page for teamId "{}"and scheduleId"{}"and entryId"{}"')
def deep_link_to_schedule_page(context, team_id, schedule_id,entryId):
    HomePage(context.browser).is_page_loaded()
    url = '{}/schedule/{}/overview'.format(context.env_variables['BASE_URL'], team_id, schedule_id,entryId)
    context.browser.get(url)




@then('I should be directed to Schedule page')
def check_landed_on_schedule_page(context):
    schedule_page = SchedulePage(context.browser)
    assert schedule_page.is_page_loaded(), 'User not directed to Schedule page after click on Schedule Tab'