from behave import *
from selenium import webdriver

@given('launch chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome("C:\iui\united-identity-main\Automated_tests")
    #context.driver=webdriver.Chrome() # you have drivres installed in python directory
    

@when('opem orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@then('verify that the log present on Page')
def verifyLogo(context):
    status=context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True

@then('close browser')
def closeBrowser(context):
    context.driver.close()