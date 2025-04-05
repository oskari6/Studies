Feature: Login Feature

  Scenario: Successful Login
    Given the user is on the login page
    When the user enters valid credentials
    And the user clicks the login button
    Then the user should be redirected to the dashboard
