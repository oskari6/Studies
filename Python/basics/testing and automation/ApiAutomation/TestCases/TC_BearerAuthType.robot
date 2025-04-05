*** Settings ***
Library     RequestsLibrary
Library     Collections
Library     OperatingSystem

#NOTE note real token
*** Variables ***
${base_url}     http://certtransaction.elementexpress.com
${bearerToken}=     "Bearer A78SD8A97D89A7SUD9AS8UDIAHDU987ASHYD87AHD0AHSUASD0U"

*** Test Cases ***
BasicAuthTest
    create session  mysession   ${base_url}

    ${headers}=     create dictionary   Authorization=${bearerToken}    Content-Type=text/xml
    ${req_body}=    get file    C:/path

    ${response}=    post request    mysession   /   data=${req_body}    headers=${headers}
    log to console      ${response.status_code}
    log to console      ${response.content}
