from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

def go_to_page(context):
    # selenium test
    context.browser.get(context.url)
    # django internal test to check for no 404 (ensure django application is running)
    response = context.test.client.get(context.url)
    # below will error out with message "AttributeError: 'HttpResponseNotFound' object has no attribute 'statuscode'" if 404 received (application not running)
    assert response.statuscode == 200

@given('I am on the log-in page')
def go_to_login_page(context):
    context.url = 'http://localhost:8000/login'
    go_to_page(context)

@given('I am on the search page')
def go_to_search_page(context):
    context.url = 'http://localhost:8000/search'
    go_to_page(context)

@given('I am on the top rated page')
def go_to_top_rated_page(context):
    context.url = 'http://localhost:8000/top_rated'
    go_to_page(context)

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

@given('I am on the my pages page of the platform')
def go_to_my_pages(context):
    set_my_pages_url(context)
    go_to_page(context)

@given('I enter some text to search for')
def search_platform(context):
    context.browser.find_element_by_name('navbar_search_field').send_keys('test search')

    And I enter some text to search for
    When I submit my search
    Then I am directed to the results page with the page results that match most closely to the text entered for my search

@when('I click on the navbar menu')
def click_on_navbar(context):
    context.browser.find_element_by_name('navbar_menu').click()

@when('I submit my search')
def submit_navbar_search(context):
    search_form = context.browser.find_element_by_name('navbar_search_form')
    context.browser.get_element(search_form, name="text").send_keys('test search')

@then('I am only shown links to the sign-up, log-in, forgotten password and about pages')
def check_logged_out_navbar_links(context):
    assert context.browser.find_element_by_name('navbar_signup').is_displayed() == True
    assert context.browser.find_element_by_name('navbar_login').is_displayed() == True
    assert context.browser.find_element_by_name('navbar_forgotten_password').is_displayed() == True
    assert context.browser.find_element_by_name('navbar_about').is_displayed() == True

@then('I am shown links to the search, create, upload document, top rated, most recent, my pages and about pages and a sign-out option.')
def check_logged_in_navbar_links(context):
    assert context.browser.find_element_by_name('navbar_search').is_displayed() == True
    assert context.browser.find_element_by_name('navbar_create').is_displayed() == True
    assert context.browser.find_element_by_name('navbar_upload_document').is_displayed() == True
    assert context.browser.find_element_by_name('navbar_top_rated').is_displayed() == True
    assert context.browser.find_element_by_name('navbar_most_recent').is_displayed() == True
    assert context.browser.find_element_by_name('navbar_my_pages').is_displayed() == True
    assert context.browser.find_element_by_name('navbar_about').is_displayed() == True
    assert context.browser.find_element_by_name('navbar_signout').is_displayed() == True

@then('I am directed to the results page with the page results that match most closely to the text entered for my search')
def check_correct_results(context):
    assert context.browser.current_url == 'http://localhost:8000/search_results'