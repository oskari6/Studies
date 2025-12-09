*** Settings ***
Library     SeleniumLibrary
Resource    ../Resources/LoginKeywords.robot

*** Variables ***
@{Browser}  Chrome
${siteUrl}  localhost:8000
${user}     test
${pwd}     123

*** Test Cases ***
LoginTest
    Open my Browser     ${siteUrl}      ${Browser}
    Enter Username      ${user}
    Enter Password      ${pwd}
    Click SignIn
    Verify Successful login
    close my browser