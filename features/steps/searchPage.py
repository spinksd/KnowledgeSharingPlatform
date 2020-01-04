from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

@given('I have the url for the search page of the knowledge sharing platform')
def set_search_page_url(context):
    context.url = 'http://localhost:8000/search'

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

@given('I am presented with a way to search the platform')
def assert_search_box_exists(context):
    assert context.browser.find_element_by_name('search_box').is_displayed() == True

@given('I enter the text \'amazon\' in the search box')
def type_amazon_into_search_box(context):
    context.browser.find_element_by_name('search_box').send_keys('amazon')

@given('I enter the text \'machine learning\' in the search box')
def type_machine_learning_into_search_box(context):
    context.browser.find_element_by_name('search_box').send_keys('machine learning')

@given('there is a page published on the platform with the word \'amazon\' in the description')
def create_page_with_amazon_in_description(context):
    assert False
    ''' # Figure out how to implement - test should be independent of other pages so can't rely on web interface for create page etc. '''

@given('the same published page has a tag of \'AWS\'')
def assert_page_has_aws_tag(context):
    assert False
    ''' # Figure out how to implement # '''

@given('the same published page has a contact of \'John Doe\'')
def assert_page_has_contact_john_doe(context):
    assert False
    ''' # Figure out how to implement # '''

@given('I click on the advanced button')
def click_advanced_search_options(context):
    context.browser.find_element_by_name('advanced_options').click()

@given('I apply a filter on a tag of \'AWS\'')
def apply_aws_tag_filter(context):
    assert False
    ''' # update #
    context.browser.find_element_by_name('tag_filter').send_keys('AWS')
    '''

@given('I apply a filter on a contact name of \'John Doe\'')
def apply_contact_filter(context):
    assert False
    ''' # update #
    context.browser.find_element_by_name('contact_filter').send_keys('John Doe')
    '''

@given('I have had at least one result to my search')
def assert_at_least_one_search_result(context):
    assert False
    ''' # update # '''

@when('I enter the url into my web browser')
def go_to_page(context):
    # selenium test
    context.browser.get(context.url)
    # django internal test to check for no 404 (ensure django application is running)
    response = context.test.client.get(context.url)
    # below will error out with message "AttributeError: 'HttpResponseNotFound' object has no attribute 'statuscode'" if 404 received (application not running)
    assert response.statuscode == 200

@given('I am on the search page')
def go_to_search_page(context):
    set_search_page_url(context)
    go_to_page(context)

@when('I click on the search button')
def submit_search(context):
    context.browser.find_element_by_name('search_button').click()

@given('I have run a search')
def run_search(context):
    type_amazon_into_search_box(context)
    submit_search(context)

@when('I click anywhere on the area of a result')
def click_on_result_area(context):
    context.browser.find_element_by_name('result1').click()

@then('I am directed to the sign-in page of the platform')
def assert_directed_to_sign_in_page(context):
    assert context.browser.current_url == 'http://localhost:8000/login'

@then('I can see the search box, most recent, my pages, top rated, upload document, create page and about tiles')
def assert_info_is_shown(context):
    assert context.browser.find_element_by_name('search_box').is_displayed() == True
    assert context.browser.find_element_by_name('most_recent').is_displayed() == True
    assert context.browser.find_element_by_name('my_pages').is_displayed() == True
    assert context.browser.find_element_by_name('top_rated').is_displayed() == True
    assert context.browser.find_element_by_name('upload_document').is_displayed() == True
    assert context.browser.find_element_by_name('create_page').is_displayed() == True
    assert context.browser.find_element_by_name('about').is_displayed() == True

@then('I am presented with the page results that match most closely to the text entered for my search')
def assert_page_results_are_shown(context):
    assert context.browser.find_element_by_name('results').is_displayed() == True

@then('I am presented with a message saying \'No results found for your search. Please try another search.\'')
def assert_no_results_message_is_shown(context):
    assert context.browser.find_element_by_name('no_results_message').is_displayed() == True

@then('I am presented with the results that match most closely to my text for my search that have the tag \'AWS\'')
def assert_results_have_tag(context):
    assert_page_results_are_shown(context)
    assert False
    ''' # update #
    assert context.browser.find_element_by_name('result1').contains('Tag:AWS')
    '''

@then('the results must have the tag \'AWS\' and must have a contact of \'John Doe\'')
def assert_results_have_tag_and_contact(context):
    assert_results_have_tag(context)
    assert False
    ''' # update #
    assert context.browser.find_element_by_name('result1').contains('Contact:John Doe')
    '''

'''
# Keeping this incase I decide to separate out the search and results pages
@then('I am directed to the editing view for the page')
def assert_directed_to_edit_view(context):
    assert context.browser.current_url.contains('edit')
'''

@then('I am taken to the published page for the result I clicked on')
def check_user_on_published_page(context):
    assert False
    '''
    set_published_page_url(context)
    go_to_page(context)
    assert context.browser.current_url == context.url
    # Figure out how to implement #

    '''