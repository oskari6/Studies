Feature: OrangeHRM Logo
    Scenario: Logo presence on OrangeHRM home Page
        Given launch chrome browser
        When opem orange hrm homepage
        Then verify that the log present on Page
        And close browser
        