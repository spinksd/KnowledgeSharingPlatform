from behave import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest

@given('I have the url for the sign-up page of the knowledge sharing platform website')
def set_url(context):
    context.url = 'http://localhost:8000/signup'

@given('I have not logged in')
def check_no_user_greeting(context):
    try:
        greeting_msg = context.browser.find_element_by_id('userGreeting')
    except NoSuchElementException:
        pass

@when('I enter the url into my web browser')
def go_to_signup_page(context):
    # selenium test
    context.browser.get(context.url)
    # django internal test to check for no 404 (ensure django application is running)
    response = context.test.client.get(context.url)
    # below will error out with message "AttributeError: 'HttpResponseNotFound' object has no attribute 'statuscode'" if 404 received (application not running)
    assert response.statuscode == 200
    
@then('the sign-up page of the website is displayed with a form requesting my forename, surname, role, email and password')
def display_signup_page(context):
    form = context.browser.find_element_by_name('signup-form')

    form_fields = []
    form_fields.append(context.browser.get_element(form, name="forename"))
    form_fields.append(context.browser.get_element(form, name="surname"))
    form_fields.append(context.browser.get_element(form, name="role"))
    form_fields.append(context.browser.get_element(form, name="email"))
    form_fields.append(context.browser.get_element(form, name="password"))

    for field in form_fields:
        assert field is not None 
    

'''
@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
'''