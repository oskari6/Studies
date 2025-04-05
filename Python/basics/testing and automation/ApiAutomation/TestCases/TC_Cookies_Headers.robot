*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***
${base_url}     http://jsonplaceholder.typicode.com

*** Test Cases ***
TestHeaders
    create session      mysession   ${base_url}
    ${response}=    get request     mysession   /photos

    ${contentTypeValue}=    get from dictionary     ${response.headers}     Content-Type
    should be equal     ${contentTypeValue}     application/json; charset=utf-8

    ${contentEncodeValue}=    get from dictionary     ${response.headers}     Content-Encoding
    should be equal     ${contentEncodeValue}     gzip
    
TextCookies
    create session      mysession   ${base_url}
    ${response}=    get request     mysession   /photos

    ${cookies_value}=   get from dictionary     ${response.cookies}     __cfduid
    