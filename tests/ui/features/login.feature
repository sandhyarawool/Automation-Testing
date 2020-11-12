Feature: Login Page

    Scenario: I can log in with correct credentials
        Given I want to log in to Hudl as Hudl Coach
        When I log in
        When I click on home Page
        Then I should be directed to my home page

    Scenario: I can log in with incorrect credentials
        Given I want to log in to Hudl as Hudl Coach
        When I log in with valid or invalid email and password
        Then I should be get an error message
        And I unble to login the page

     Scenario: I can log in with need help
        Given I want to log in to Hudl as Hudl Coach
        When I log in with need help
        Then I should see an option to reset password

    
    