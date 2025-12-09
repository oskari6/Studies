*** Settings ***
Library     JSONLibrary
Library     RequestsLibrary
Library     os
Library     Collections

*** Variables ***
${base_url}     https://restcountries.eu

*** Test Cases ***
GetCountryInfo
    create session      mysession   ${base_url}
    ${response}=    get request     mysession   /rest/v2/alpha/IN

    ${json_obj}=    to json     ${response.content}

    #single data validation array
    ${border}=     get value from json     ${json_obj}     $.borders[0]
    log to console  ${border[0]}
    should be equal     ${border[0]}   AFG

    #multiple data validation in array
    ${borders}=     get value from json     ${json_obj}     $.borders
    log to console      ${borders[0]}
    should contain any      ${borders[0]}   AFG     BGD     BTN     MMR     ABC
    should not contain any  ${borders[0]}   abc     xyz
    
