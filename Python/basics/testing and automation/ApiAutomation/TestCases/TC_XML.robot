*** Settings ***
Library     XML
Library     OS
Library     Collections

#<employees>
#    <employee id="be129">
#        <firstname>John</firstname>
#        <lastname>Doe</lastname>
#        <title>Engineer</title>
#        <division>Materials</division>
#        <building>327</building>
#        <room>19</room>
#        <supervisor>be131</supervisor>
#    </employee>
#</employees>

*** Test Cases ***
TestCase1
    ${xml_obj}=     parse_xml   C:/SeleniumPractice/xmldata/employees.xml

    #validations
    #direct
    ${emp_firstname}=   get element text    ${xml_obj}      .//employee[1]/firstname
    should be equal     ${emp_firstname}    John

    #indirect
    ${emp_firstname}=   get element     ${xml_obj}      .//employee[1]/firstname
    should be equal     ${emp_firstname.text}   John

    element text should be  ${xml_obj}      John    .//employee[1]/firstname

    ${count}=   get element count   ${xml_obj}      .//employee
    should be equal     ${count}    6

    element attribute should be     ${xml_obj}      id  be129       .//employee[1]

    ${child_elements}=   get child elements      ${xml_obj}      .//employee[1]
    should not be empty     ${child_elements}

    ${fname}=   get element text    ${child_elements[0]}