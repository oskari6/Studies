#pip install robotframework-databaselibrary
#pip install pyodbc

*** Settings ***
Library     DatabaseLibrary

*** Variables ***
${DB_DRIVER}    ODBC Driver 17 for SQL Server
${DB_SERVER}    localhost\\SQLEXPRESS
${DB_NAME}      DEVELOP
${DB_USER}      oskari
${DB_PASSWORD}  admin123

*** Test Cases ***
Connect to SQL Server and Fetch data
    [Documentation]     Connect to the SQL Server database and retrieve data
    Connect To Database    pyodbc    DRIVER={${DB_DRIVER}};SERVER=${DB_SERVER};DATABASE=${DB_NAME};UID=${DB_USER};PWD=${DB_PASSWORD}
    @{query_results}    Query    SELECT TOP 5 * FROM PPM.T_USER;
    Log Many    ${query_results}
    Disconnect From Database