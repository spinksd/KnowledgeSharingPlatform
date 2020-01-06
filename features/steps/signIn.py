from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException

@given('I have the url for the sign-in page of the knowledge sharing platform')
def set_sign_in_url(context):
    context.url = 'http://localhost:8000/login'

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

@given('I am on the sign-in page of the platform')
def go_to_sign_in_page(context):
    set_sign_in_url(context)
    go_to_page(context)

@given('I enter valid credentials into the sign-in form')
def enter_sign_up_form_details(context):
    form = context.browser.find_element_by_name('login_form')

    context.browser.get_element(form, name="email").send_keys('test.user@example.com')
    context.browser.get_element(form, name="password").send_keys('insecurepassword')
    ''' Alternative implementation
    context.browser.find_element_by_name('username_field').send_keys('Joe')
    context.browser.find_element_by_name('surname_field').send_keys'Bloggs')
    context.browser.find_element_by_name('role_field').send_keys('Software Engineer')
    context.browser.find_element_by_name('email_field').send_keys('Joe.Bloggs@example.com')
    context.browser.find_element_by_name('password_field').send_keys('insecurepassword')
    '''

@given('I enter invalid credentials into the sign-in form')
def enter_invalid_sign_up_form_details(context):
    form = context.browser.find_element_by_name('login_form')

    context.browser.get_element(form, name="email").send_keys('fake.acount@doesntexist.com')
    context.browser.get_element(form, name="password").send_keys('thiswillfail')

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

@when('I click on the sign-up button')
def click_login_button(context):
    context.browser.find_element_by_name('sign_up_button').click()

@when('I click on the \'forgotten password\' button')
def click_forgotten_password_button(context):
    context.browser.find_element_by_name('forgotten_password_button').click()

@then('the sign-in page of the platform is displayed asking me to log in or sign up')
def display_sign_in_page(context):
    form = context.browser.find_element_by_name('login_form')

    context.browser.get_element(form, name="email")
    context.browser.get_element(form, name="password")

@then('I am directed to the search page of the platform')
def check_directed_to_search_page(context):
    assert context.browser.current_url == 'http://localhost:8000/search'

@then('I should be logged in')
def confirm_logged_in(context):
    check_logged_in(context)

@then('I should not be logged in')
def confirm_not_logged_in(context):
    check_not_logged_in(context)

@then('I should be presented with a message saying \'Your credentials are invalid, please try again.\'')
def check_user_creation_message(context):
    alert_text = Alert(context.browser).textalert
    #alert = context.browser.find_element_by_name('alert')   
    assert alert_text == 'Your credentials are invalid, please try again.'

@then('I should be directed to the sign-up page')
def check_directed_to_login_page(context):
    assert context.browser.current_url == 'http://localhost:8000/signup'
    
@then('I should be directed to the forgotten password page')
def check_directed_to_forgotten_password_page(context):
    assert context.browser.current_url == 'http://localhost:8000/forgotten_password'