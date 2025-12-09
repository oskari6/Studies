*** Settings ***
Library     SeleniumLibrary
Suite Teardown      Close Browser
*** Variables ***
${Login-Url}    http://localhost/robot
${Browser}      Chrome
*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Type In Username    demo
    Type In Password    mode
    Sleep   3s
    Submit Credentials
    Welcome Page Should Be Open

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${Login-Url}   ${Browser}
    Title Should Be     Login Page

Type In Username
    [Arguments]     ${username}
    Input Text      id=username_field   ${username}

Type In Password
    [Arguments]     ${password}
    Input Text      id=password_field   ${password}

Submit Credentials
    Click Button    id=login_button

Welcome Page Should be Open
    Title Should Be     Welcome Page