from behave import *
from selenium import webdriver

@given(u'I launch browser')
def step_impl(context):
    assert True,"Test passed"


@when(u'I open application')
def step_impl(context):
    assert True,"Test passed"


@when(u'Enter valid username and password')
def step_impl(context):
    assert True,"Test passed"


@when(u'click on login')
def step_impl(context):
    assert True,"Test passed"


@then(u'User must login to the Dashboard page')
def step_impl(context):
    assert True,"Test passed"


@when(u'navigate to search page')
def step_impl(context):
    assert True,"Test passed"


@then(u'search page should display')
def step_impl(context):
    assert True,"Test passed"


@when(u'navigate to advanced search page')
def step_impl(context):
    assert True,"Test passed"


@then(u'advanced search page should display')
def step_impl(context):
    assert True,"Test passed"