from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

@given('I have the url for a published page of the knowledge sharing platform')
def set_published_page_url(context):
    assert False
    '''
    # Figure out how to implement this #
    context.url = 'http://localhost:8000/'
    '''

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

@given('I am on a published page that was created by my user')
def go_to_published_page(context):
    set_published_page_url(context)
    go_to_page(context)

@given('I am provided with a button to edit the page')
def assert_edit_button_exists(context):
    assert context.browser.find_element_by_name('edit_button').is_displayed() == True

@when('I enter the url into my web browser')
def go_to_page(context):
    # selenium test
    context.browser.get(context.url)
    # django internal test to check for no 404 (ensure django application is running)
    response = context.test.client.get(context.url)
    # below will error out with message "AttributeError: 'HttpResponseNotFound' object has no attribute 'statuscode'" if 404 received (application not running)
    assert response.statuscode == 200

@when('I click on the edit button')
def click_on_page_area(context):
    context.browser.find_element_by_name('edit_button').click()

@then('I am directed to the sign-in page of the platform')
def assert_directed_to_sign_in_page(context):
    assert context.browser.current_url == 'http://localhost:8000/login'

@then('I can see the title, description, tags, document (if exists) and contact information for the page')
def assert_info_is_shown(context):
    assert context.browser.find_element_by_name('title').is_displayed() == True
    assert context.browser.find_element_by_name('description').is_displayed() == True
    assert context.browser.find_element_by_name('tags').is_displayed() == True
    assert context.browser.find_element_by_name('contacts').is_displayed() == True
    if not context.driver.find_elements_by_name('document'):
        # List is empty (Document does not exist on page as this page does not have a document) - so pass test
        pass
    else:
        # List is not empty (Page does have document within it)
        assert context.browser.find_element_by_name('document').is_displayed

@then('I am directed to the editing view for the page')
def assert_directed_to_edit_view(context):
    assert context.browser.current_url.contains('edit')

@then('I am directed to the published page')
def check_user_on_published_page(context):
    assert False
    '''
    set_published_page_url(context)
    go_to_page(context)
    assert context.browser.current_url == context.url
    # Figure out how to implement #

    '''