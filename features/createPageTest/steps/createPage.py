from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

@given('I have the url for the create page of the knowledge sharing platform')
def set_create_url(context):
    context.url = 'http://localhost:8000/create_page'

@given('I am not logged in')
def check_not_logged_in(context):
    context.b
    try:
        login_option = context.browser.find_element_by_id('nav-login')
    except NoSuchElementException:
        raise NoSuchElementException

@given('I am logged in')
def log_in(context):
    context.browser.get('http://localhost:8000/')
    try:
        login_option = context.browser.find_element_by_id('nav-login')
        context.browser.find_element_by_id('id_username').send_keys('DSPINKS')
        context.browser.find_element_by_id('id_password').send_keys('testing321')
        context.browser.find_element_by_id('id_submit').click()
        time.sleep(2)
        assert context.browser.find_element_by_id('nav-profile') is not None
    except NoSuchElementException:
        raise NoSuchElementException

@when('I enter the url into my web browser')
def go_to_page(context):
    # selenium test
    context.browser.get(context.url)
    # django internal test to check for no 404 (ensure django application is running)
    response = context.test.client.get(context.url)
    # below will error out with message "AttributeError: 'HttpResponseNotFound' object has no attribute 'statuscode'" if 404 received (application not running)
    assert response.statuscode == 200

@given('I am on the create page')
def go_to_create_page(context):
    set_create_url(context)
    go_to_page(context)
    assert context.browser.current_url() == 'http://localhost:8000/create_page'

@when('I click on the text box for the title of the page')
def click_title_box(context):
    context.browser.find_element_by_id('title').click()

@when('I click on the text box for the description of the page')
def click_description_box(context):
    context.browser.find_element_by_id('text').click()

@when('I click on the tags section of the page')
def click_tags_box(context):
    context.browser.find_element_by_id('tags').click()

@when('I click on the contacts section of the page')
def click_contacts_box(context):
    context.browser.find_element_by_id('contacts').click()

@when('I click on the publish button')
def publish_page(context):
    context.browser.find_element_by_id('publish-page-button').click()

@then('I am directed to the sign-in page of the platform')
def check_directed_to_sign_in_page(context):
    assert context.browser.current_url == 'http://localhost:8000/login'

@then('I can edit the title, description, tags and contacts information')
def check_editable_information(context):
    assert context.browser.find_element_by_id('title').is_displayed() == True
    assert context.browser.find_element_by_id('title').is_enabled() == True
    assert context.browser.find_element_by_id('text').is_displayed() == True
    assert context.browser.find_element_by_id('text').is_enabled() == True
    assert context.browser.find_element_by_id('tags').is_displayed() == True
    assert context.browser.find_element_by_id('tags').is_enabled() == True
    assert context.browser.find_element_by_id('contacts').is_displayed() == True
    assert context.browser.find_element_by_id('contacts').is_enabled() == True

@then('My user will be the default contact in the contacts section')
def check_default_contact(context):
    assert False
    '''
    #FIGURE OUT HOW I CAN DO THIS#
    contact = context.browser.find_element_by_name('contact1').text
    assert contact.contains('')
    '''

@then('I can edit the text and update it to the title of my choice')
def update_title(context):
    context.browser.find_element_by_name('title').send_keys('AUTOMATED TESTS - TITLE TEST')
    assert context.browser.find_element_by_name('title').text.contains('AUTOMATED TESTS - TITLE TEST')

@then('I can edit the text and update it to the description of my choice')
def update_description(context):
    context.browser.find_element_by_name('description').send_keys('This is a test that updates the description of the page to be created.')
    assert context.browser.find_element_by_name('description').text.contains('This is a test that updates the description of the page to be created.')

@then('I can edit the tags and update it to the tags of my choice')
def update_tags(context):
    assert False
    '''
    #Update this when decided on implementation#
    context.browser.find_element_by_name('tags').send_keys('test-tag')
    assert context.browser.find_element_by_name('tags').text.contains('test-tag')
    '''

@then('I can edit the contact list and update it with the users of my choice')
def update_contacts(context):
    assert False
    '''
    #Update this when decided on implementation#
    context.browser.find_element_by_name('contacts').send_keys('Joe Bloggs')
    assert context.browser.find_element_by_name('contacts').text.contains('Joe Bloggs')
    '''

@then('my user must always be on the list')
def check_my_user_in_contacts(context):
    check_default_contact(context)

@given('I am happy with the information on the page')
def update_page_info(context):
    update_title(context)
    update_description(context)
    update_tags(context)
    update_contacts(context)

@then('the page should be published on the platform')
def check_page_is_published(context):
    assert False
    '''
    # Figure out how to implement #
    ''' 

@then('I am directed to the published page')
def check_user_on_published_page(context):
    assert False
    '''
    # Figure out how to implement #
    '''