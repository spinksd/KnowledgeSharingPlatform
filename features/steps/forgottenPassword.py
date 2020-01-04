from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException

@given('I have the url for the forgotten password page of the knowledge sharing platform')
def set_forgotten_password_url(context):
    context.url = 'http://localhost:8000/forgotten_password'

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

@given('I am on the forgotten password page')
def go_to_forgotten_password_page(context):
    set_forgotten_password_url(context)
    go_to_page(context)

@given('I enter an email that is associated with an account into the form')
def enter_forgotten_password_form_details(context):
    form = context.browser.find_element_by_name('retrieval_form')

    context.browser.get_element(form, name="email").send_keys('test.user@example.com')
    ''' Alternative implementation
    context.browser.find_element_by_name('email_field').send_keys('test.user@example.com')
    '''

@given('I enter an email that is not associated with an account into the form')
def enter_invalid_forgotten_password_form_details(context):
    form = context.browser.find_element_by_name('retrieval_form')

    context.browser.get_element(form, name="email").send_keys('fake.user@emaildoesntexist.com')
    ''' Alternative implementation
    context.browser.find_element_by_name('username_field').send_keys('Joe')
    context.browser.find_element_by_name('surname_field').send_keys'Bloggs')
    context.browser.find_element_by_name('role_field').send_keys('Software Engineer')
    context.browser.find_element_by_name('email_field').send_keys('Joe.Bloggs@example.com')
    context.browser.find_element_by_name('password_field').send_keys('insecurepassword')
    '''

@when('I enter the url into my web browser')
def go_to_page(context):
    # selenium test
    context.browser.get(context.url)
    # django internal test to check for no 404 (ensure django application is running)
    response = context.test.client.get(context.url)
    # below will error out with message "AttributeError: 'HttpResponseNotFound' object has no attribute 'statuscode'" if 404 received (application not running)
    assert response.statuscode == 200
    
@when('I press submit')
def submit_signup_form(context):
    form = context.browser.find_element_by_name('login_form')
    context.get_element(form, name='submit').click()
    #context.browser.find_element_by_name('submit_signup').click()

@when('I click on the login button')
def click_login_button(context):
    context.browser.find_element_by_name('login_button').click()

@then('the forgotten password page of the website is displayed with a form requesting the email that\'s associated with the account')
def display_sign_in_page(context):
    form = context.browser.find_element_by_name('login_form')

    context.browser.get_element(form, name="email")
    context.browser.get_element(form, name="password")

@then('I am directed to the search page of the platform')
def check_directed_to_search_page(context):
    assert context.browser.current_url == 'http://localhost:8000/search'

@then('I should be presented with a message saying \'You need to be logged out to access that page.\'')
def check_invalid_navigation_message(context):
    alert_text = Alert(context.browser).text
    #alert = context.browser.find_element_by_name('alert')   
    assert alert_text == 'You need to be logged out to access that page.'

@then('I should be presented with a message saying \'An email has been sent to the user\'s email address if exists. Please follow the instructions on the email to reset your password.\'')
def check_email_sent_message(context):
    alert_text = Alert(context.browser).text
    #alert = context.browser.find_element_by_name('alert')   
    assert alert_text == 'You need to be logged out to access that page.'

@then('I should be directed to the login page')
def check_directed_to_login_page(context):
    assert context.browser.current_url == 'http://localhost:8000/login'
