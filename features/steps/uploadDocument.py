import os
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException

@given('I have the url for the upload document page of the knowledge sharing platform')
def set_upload_document_url(context):
    context.url = 'http://localhost:8000/upload_document'

@given('I am not logged in')
def check_not_logged_in(context):
    try:
        greeting_msg = context.browser.find_element_by_name('user_greeting')
    except NoSuchElementException:
        pass

@given('I am logged in')
def check_logged_in(context):
    try:
        greeting_msg = context.browser.find_element_by_name('user_greeting')
    except NoSuchElementException:
        raise NoSuchElementException

@given('I provide a valid document to upload in the upload form')
def select_valid_test_document(context):
    context.browser.find_element_by_id("document_upload_selector").send_keys(os.path.dirname(os.path.abspath(__file__)) + '../files/upload_valid_test_document.docx')

@given('I provide an invalid document to upload')
def select_invalid_test_document(context):
    context.browser.find_element_by_id("document_upload_selector").send_keys(os.path.dirname(os.path.abspath(__file__)) + '../files/upload_invalid_test_document.exe')

@when('I enter the url into my web browser')
def go_to_page(context):
    # selenium test
    context.browser.get(context.url)
    # django internal test to check for no 404 (ensure django application is running)
    response = context.test.client.get(context.url)
    # below will error out with message "AttributeError: 'HttpResponseNotFound' object has no attribute 'statuscode'" if 404 received (application not running)
    assert response.statuscode == 200

@given('I am on the upload document page')
def go_to_my_pages(context):
    set_upload_document_url(context)
    go_to_page(context)

@when('I press submit')
def upload_test_document(context):
    context.driver.find_element_by_id("submit").click()

@then('I am directed to the sign-in page of the platform')
def check_directed_to_sign_in_page(context):
    assert context.browser.current_url == 'http://localhost:8000/login'

@then('I should be presented with a way to upload a document to the platform')
def assert_document_upload_is_shown(context):
    assert context.browser.find_element_by_name('document_upload_button').is_displayed() == True

@then('I should be directed to the create page with the title, description and tags automatically generated and populated')
def assert_create_page_populated(context):
    assert context.browser.find_element_by_name('title').is_displayed() == True
    assert context.browser.find_element_by_name('title').text() is not None
    assert context.browser.find_element_by_name('description').is_displayed() == True
    assert context.browser.find_element_by_name('description').text() is not None
    assert context.browser.find_element_by_name('tags').is_displayed() == True
    assert context.browser.find_element_by_name('tags').text() is not None

@then('I can review and edit the generated information before publishing the page')
def assert_create_page_info_is_editable(context):
    assert context.browser.find_element_by_name('title').is_enabled() == True
    assert context.browser.find_element_by_name('description').is_enabled() == True
    assert context.browser.find_element_by_name('tags').is_enabled() == True

@then('I should be presented with a message saying \'Invalid document selected, please upload a valid document.\'')
def check_invalid_document_message(context):
    alert_text = Alert(context.browser).textalert
    #alert = context.browser.find_element_by_name('alert')   
    assert alert_text == 'Invalid document selected, please upload a valid document.'