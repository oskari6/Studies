*** Settings ***
Library     SeleniumLibrary
Resource    ../Resources/RegistrationKeywords.robot

***  Variables ***
${browser}      Chrome
${SiteUrl}      localhost:8000

*** Test Cases ***
Open my Browser           ${SiteUrl}    ${Browser}
Click Register Link
Enter FirstName           David
Enter LastName            John
Enter Phone               1234567890
Enter Email               davidJohn@gmail.com
Enter Address1            Toronto
Enter Address2            Canada
Enter City                Toronto
Enter State               Brampton
Enter Postal Code         L3S 1E7
Select Country            CANADA
Enter User Name           johnxyz
Enter Password            johnxyz
Enter Confirmed Password  johnxyz
Click Submit
Verify Successful Registration
close my browsers