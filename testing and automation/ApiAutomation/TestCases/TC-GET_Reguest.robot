*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variable ***
@{base_url}      http://restapi.demoqa.com/customer

*** Test Cases ***
Put_CustomerRegistration
    create session  mysession   ${base_url}
    ${body}=    create dictionary   FirstName=test1   LastName=test2
    ${header}=  create dictionary   Contenty-Type=application/json
    ${response}=    post request    mysession /register     data=${body}    headers=${header}

    log to console  ${response.status_code}
    log to console  ${response.content}

    #Validations

    ${status_code}=     convert to string   ${response.status_code}
    should be equal     ${status_code}      201
    ${res_body}=    convert to string   ${response.content}
    should contain      ${res_body}     OPERATION_SUCCESS
    should contain      ${res_body}     Operation completed succesfully

    