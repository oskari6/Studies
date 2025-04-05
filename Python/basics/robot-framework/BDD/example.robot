*** Settings ***
Library    GherkinLibrary
Library    SeleniumLibrary

*** Keywords ***
Given the user is on the login page
    Open Browser    https://example.com/login    Chrome

When the user enters valid credentials
    Input Text    username_field    user123
    Input Text    password_field    pass123

And the user clicks the login button
    Click Button    login_button

Then the user should be redirected to the dashboard
    Page Should Contain    Welcome to the Dashboard