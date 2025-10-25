*** Settings ***
Library     SeleniumLibrary
Variables   ../PageObjects/Locators.py

*** Keywords ***
Open my Browser
    [Arguments]    ${SiteUrl}    ${Browser}
    open browser    ${SiteUrl}    ${Browser}
    Maximize Browser Window

Click Register Link
    click link    ${link_Reg}

Enter FirstName
    [Arguments]    ${firstName}
    Input Text    ${txt_firstName}    ${firstName}

Enter LastName
    [Arguments]    ${lastName}
    Input Text    ${txt_lastName}    ${lastName}

Enter Phone
    [Arguments]    ${phone}

Enter Email
    [Arguments]     ${email}
    Input Text      ${txt_email}    ${email}

Enter Address1
    [Arguments]     ${add1}
    Input Text      ${txt_add1}     ${add1}
    
Enter Address2
    [Arguments]    ${add2}
    Input Text    ${txt_add2}    ${add2}

Enter City
    [Arguments]    ${city}
    Input Text    ${txt_city}    ${city}

Enter State
    [Arguments]    ${state}
    Input Text    ${txt_state}    ${state}

Enter Postal Code
    [Arguments]    ${postalcode}
    Input Text    ${txt_postCode}    ${postalcode}

Select Country
    [Arguments]    ${country}
    select from list by label    ${drp_country}    ${country}

Enter User Name
    [Arguments]    ${username}
    Input Text    ${txt_userName}    ${username}

Enter Password
    [Arguments]    ${password}
    Input Text    ${txt_Password}    ${password}

Enter Confirmed Password
    [Arguments]    ${confpassword}
    Input Text    ${txt_conformedPassword}    ${confpassword}

Click Submit
    click button    ${btn_submit}

Verify Successful Registration
    page should contain    Thank you for registering.

close my browsers
    close all browsers