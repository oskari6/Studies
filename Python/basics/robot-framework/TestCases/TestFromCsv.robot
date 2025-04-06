*** Settings ***
Library     SeleniumLibrary
Resource    ../Resources/LoginKeywords.robot
Library     DataDriver  ../TestData/LoginData.csv

Suite Setup     Open my browser
Suite Teardown      Close Browsers
Test Template   Invalid Login

*** Test Cases ***
LoginTextWithCsv using ${username} and ${password}

*** Keywords ***
    [Arguments]     ${username}     ${password}
    Input username    ${username}
    Input pwd   ${password}
    click login button
    Error message should be visible
      