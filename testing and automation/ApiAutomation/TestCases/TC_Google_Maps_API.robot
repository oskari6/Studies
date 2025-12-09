*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***
${base_url}     https://maps.googleApis.com
${req_uri}      /maps/api/place/nearbysearch/json?

*** Test Cases ***
GoogleMapPlacesAPITC
    create session      mysession    ${base_url}
    ${params}=      create dictionary   location=-33.8670522, 151.1957362   radius=500  types=food  name=harbour    key=api_key_here
    ${response}=    get request     mysession       ${req_uri}       params=${params}

    log to console      ${response.status_code}
    log to console      ${response.content}
