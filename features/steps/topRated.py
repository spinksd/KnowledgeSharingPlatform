from behave import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

@given('I have the url for the top rated page of the knowledge sharing platform')
def set_top_rated_url(context):
    context.url = 'http://localhost:8000/top_rated'

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

@given('I am on the top rated page')
def go_to_top_rated(context):
    set_top_rated_url(context)
    go_to_page(context)

@given('I am presented with a view of the top rated pages')
def assert_presented_view_top_rated_pages(context):
    assert context.browser.find_element_by_name('top_rated_pages').is_displayed() == True

@when('I enter the url into my web browser')
def go_to_page(context):
    # selenium test
    context.browser.get(context.url)
    # django internal test to check for no 404 (ensure django application is running)
    response = context.test.client.get(context.url)
    # below will error out with message "AttributeError: 'HttpResponseNotFound' object has no attribute 'statuscode'" if 404 received (application not running)
    assert response.statuscode == 200

@when('I click anywhere on the area of a top rated page')
def click_on_page_area(context):
    context.browser.find_element_by_name('page1').click()

@then('I am directed to the sign-in page of the platform')
def check_directed_to_sign_in_page(context):
    assert context.browser.current_url == 'http://localhost:8000/login'

@then('I should see a message saying \'There have not been any published pages liked.\'')
def check_no_liked_pages_message(context):
    assert context.browser.find_element_by_name('no_liked_pages_message').is_displayed() == True
    assert context.browser.find_element_by_name('no_liked_pages_message').text.contains('There have not been any published pages liked.')

@then('I am directed to the published page for the page I clicked on')
def check_user_on_published_page(context):
    assert False
    '''
    # Figure out how to implement #
    '''