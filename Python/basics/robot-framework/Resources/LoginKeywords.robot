*** Settings ***
Library SeleniumLibrary
Variables   ../PageObjects/Locators.py

*** Keywords ***
Open my Browser
    [Arguments]     ${siteUrl}      ${browser}
    Open Browser    ${siteUrl}      ${browser}
    Maximize Browser Window

Enter Username
    [Arguments]     ${username}
    Input Text      ${txt_loginUserName}    ${username}

Enter Password
    [Arguments]     ${password}
    Input Text      ${txt_loginPassword}    ${password}

Click SignIn
    Click button    ${btn_signIn}

Verify Successful Login
    Title Should Be     Right Title

Close My Browsers
    close all browsers