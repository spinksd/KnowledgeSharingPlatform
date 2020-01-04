from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException

@given('I have the url for the signup page of the platform')
def set_sign_up_url(context):
    context.url = 'http://localhost:8000/signup'

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

@given('I am on the signup page of the platform')
def go_to_sign_up_page(context):
    set_sign_up_url(context)
    go_to_page(context)

@given('I enter valid details into the signup form')
def enter_sign_up_form_details(context):
    form = context.browser.find_element_by_name('signup_form')

    context.browser.get_element(form, name="forename").send_keys('Joe')
    context.browser.get_element(form, name="surname").send_keys('Bloggs')
    context.browser.get_element(form, name="role").send_keys('Software Engineer')
    context.browser.get_element(form, name="email").send_keys('Joe.Bloggs@example.com')
    context.browser.get_element(form, name="password").send_keys('insecurepassword')
     ''' Alternative implementation
    context.browser.find_element_by_name('username_field').send_keys('Joe')
    context.browser.find_element_by_name('surname_field').send_keys'Bloggs')
    context.browser.find_element_by_name('role_field').send_keys('Software Engineer')
    context.browser.find_element_by_name('email_field').send_keys('Joe.Bloggs@example.com')
    context.browser.find_element_by_name('password_field').send_keys('insecurepassword')
    '''

@given('I enter invalid details into the signup form')
def enter_invalid_sign_up_form_details(context):
    form = context.browser.find_element_by_name('signup_form')

    context.browser.get_element(form, name="forename").send_keys('@3139amcda?.,z')
    context.browser.get_element(form, name="surname").send_keys('orif1=1;show databases;')
    context.browser.get_element(form, name="role").send_keys('hacker')
    context.browser.get_element(form, name="email").send_keys('spam.box@spam.com')
    context.browser.get_element(form, name="password").send_keys('')

@given('the email I have entered is already in use by an account')
def duplicate_account(context):
    submit_sign_up_form()
    enter_sign_up_form_details()

@when('I enter the url into my web browser')
def go_to_page(context):
    # selenium test
    context.browser.get(context.url)
    # django internal test to check for no 404 (ensure django application is running)
    response = context.test.client.get(context.url)
    # below will error out with message "AttributeError: 'HttpResponseNotFound' object has no attribute 'statuscode'" if 404 received (application not running)
    assert response.statuscode == 200
    
@when('I press submit')
def submit_sign_up_form(context):
    form = context.browser.find_element_by_name('signup_form')
    context.get_element(form, name='submit').click()
    #context.browser.find_element_by_name('submit_signup').click()

@when('I click on the login button')
def click_login_button(context):
    context.browser.find_element_by_name('login_button').click()

@when('I click on the \'forgotten password\' button/link')
def click_forgotten_password_button(context):
    context.browser.find_element_by_name('forgotten_password').click()

@then('the signup page of the platform is displayed with a form requesting my forename, surname, role, email and password')
def display_signup_page(context):
    form = context.browser.find_element_by_name('signup_form')

    context.browser.get_element(form, name="forename")
    context.browser.get_element(form, name="surname")
    context.browser.get_element(form, name="role")
    context.browser.get_element(form, name="email")
    context.browser.get_element(form, name="password")

@then('I am directed to the search page of the platform')
def check_directed_to_search_page(context):
    assert context.browser.current_url == 'http://localhost:8000/search'

@then('I should have a user created with the details I entered')
def confirm_user_created(context):
    assert False
    '''
    Fill in with connection to mysql backend
    '''

@then('I should be directed to the login page')
def check_directed_to_login_page(context):
    assert context.browser.current_url == 'http://localhost:8000/login'
    
@then('I should be presented with a message saying \'User succesfully created.\'')
def check_user_creation_message(context):
    alert_text = Alert(context.browser).text
    #alert = context.browser.find_element_by_name('alert')   
    assert alert_text == 'User successfully created.'

@then('I should have a user created')
def confirm_user_not_created(context):
    assert False
    '''
    Fill in with connection to mysql backend
    '''

@then('I should be presented with a message saying \'Your details are invalid, please try again.\'')
def check_user_creation_error_message(context):
    alert_text = Alert(context.browser).text
    #alert = context.browser.find_element_by_name('alert')   
    assert alert_text == 'Your details are invalid, please try again.'

@then('I should not have a duplicate user created')
def confirm_no_duplicate_user(context):
    assert False
    '''
    Fill in with connection to mysql backend
    '''

@then('I should be presented with a message saying \'A user has already been created for this email. Please request a new password via the \'Forgotten Password?\' link.\'')
def check_duplicate_email_message(context):
    alert_text = Alert(context.browser).text
    #alert = context.browser.find_element_by_name('alert')   
    assert alert_text == 'A user has already been created for this email. Please request a new password via the \'Forgotten Password?\' link.'

@then('I should be directed to the forgotten password page')
def check_directed_to_forgotten_password_page(context):
    assert context.browser.current_url == 'http://localhost:8000/forgotten_password'