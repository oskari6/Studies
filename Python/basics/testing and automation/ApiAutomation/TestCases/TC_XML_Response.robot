*** Settings ***
Library     XML
Library     RequestsLibrary
Library     os
Library     Collections

*** Variables ***
${base_url}     https://thomas-bayer.com

*** Test Cases ***
TestCase1
    create session      mysession   ${base_url}
    ${response}=    get request     mysession   /sqlrest/CUSTOMER/15

    ${xml_string}=    convert to string     ${response.content}
    ${xml_obj}=     parse xml   ${xml_string}

    element text should be      ${xml_obj}      15      .//ID
    