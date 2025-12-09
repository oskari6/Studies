*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variable ***
@{base_url}      http://restapi.demoqa.com
@{city}     Delphi

*** Test Cases ***
Get_weatherInfo
    create session  myssion     ${base_url}
    ${response}=    get request     myssion     /utilities/weather/city/${city}
    log to console  ${response.status_code}
    log to console ${response.content}
    log to console ${response.headers}

    #Validations
    ${status_code}=     convert to string   ${response.status_code}
    should be equal     ${status_code}      200

    ${body}=    convert to string       ${response.content}
    should contain  ${body}     Delphi

    ${contentTypeValue}=    get from dicitonary     ${response.headers}     Content-Type
    should be equal     ${contentTypeValue}     application/json
    