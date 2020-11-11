Feature: Schedule Page

    Scenario: I can log in with correct credentials
        Given I want to log in to Hudl as Hudl Coach
        When I log in
        When I click on home Page
        When I click on Teams Dropdown
        When I click on Schedule Tab
        #When I deep link to schedule page for teamId "{}"and scheduleId"{}"
        Then I should be directed to Schedule page