from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I have the url for the edit page of a published page that was created by my user')
def set_edit_url(context):
    context.url = 'http://localhost:8000/{published_page}/edit'
    assert False
    '''
    Figure out how to implement the above
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

@when('I enter the url into my web browser')
def go_to_page(context):
    # selenium test
    context.browser.get(context.url)
    # django internal test to check for no 404 (ensure django application is running)
    response = context.test.client.get(context.url)
    # below will error out with message "AttributeError: 'HttpResponseNotFound' object has no attribute 'statuscode'" if 404 received (application not running)
    assert response.statuscode == 200

@given('I am editing a published page that was created by my user')
def go_to_edit_page(context):
    context.url = 'http://localhost:8000/my_pages'
    go_to_page(context)
    # Wait until page 1 is clickable
    element = WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.ID, "page1")))
    element.click()
    # Wait until edit button is clickable
    element = WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.ID, "edit_button")))
    element.click()
    assert context.url.contains('edit')

@given('I click on the text box for the title of the page')
def click_title_box(context):
    context.browser.find_element_by_name('title').click()

@given('I click on the text box for the description of the page')
def click_description_box(context):
    context.browser.find_element_by_name('description').click()

@given('I click on the tags section of the page')
def click_tags_box(context):
    context.browser.find_element_by_name('tags').click()

@given('I click on the contacts section of the page')
def click_contacts_box(context):
    context.browser.find_element_by_name('contacts').click()

@given('I am provided with a button to publish the page')
def check_publish_button_exists(context):
    assert context.browser.find_element_by_name('publish_button').is_displayed() == True
    assert context.browser.find_element_by_name('publish_button').is_enabled() == True

@when('the editing page has loaded')
def check_edit_page_loaded(context):
    # Wait for elements on page to load
    try:
        WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.ID, "publish_button")))
        WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.ID, "title")))
        WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.ID, "description")))
        WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.ID, "tags")))
        WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.ID, "contacts")))
    except TimeoutException:
        print('Loading edit page took too long!')
        assert False

@when('I remove the current title and type in the title to be \'test title - edited\'')
def update_title(context):
    context.browser.find_element_by_name('title').clear()
    '''
    alternative to above if it doesn't work:
    webElement.sendKeys(Keys.CONTROL + "a");
    webElement.sendKeys(Keys.DELETE);
    '''
    context.browser.find_element_by_name('title').send_keys('test title - edited')


@when('I remove the current description and type in the description to be \'test description - edited\'')
def update_description(context):
    context.browser.find_element_by_name('description').clear()
    context.browser.find_element_by_name('description').send_keys('test description - edited')

@when('I remove the current tags and add a tag \'test tag - edited\'')
def update_tags(context):
    assert False
    ''' Need to figure out how to implement '''

@when('I remove any current additional contacts and add a contact \'test contact - edited\'')
def update_contacts(context):
    assert False
    ''' Need to figure out how to implement '''

@when('I click on the publish button')
def publish_page(context):
    context.browser.find_element_by_name('publish_button').click()

@then('I am directed to the sign-in page of the platform')
def check_directed_to_sign_in_page(context):
    assert context.browser.current_url == 'http://localhost:8000/login'

@then('I am directed to the search page of the platform')
def check_directed_to_sign_in_page(context):
    assert context.browser.current_url == 'http://localhost:8000/search'

@then('I can edit the title, description, tags and contacts information')
def check_editable_information(context):
    assert context.browser.find_element_by_name('title').is_displayed() == True
    assert context.browser.find_element_by_name('title').is_enabled() == True
    assert context.browser.find_element_by_name('description').is_displayed() == True
    assert context.browser.find_element_by_name('description').is_enabled() == True
    assert context.browser.find_element_by_name('tags').is_displayed() == True
    assert context.browser.find_element_by_name('tags').is_enabled() == True
    assert context.browser.find_element_by_name('contacts').is_displayed() == True
    assert context.browser.find_element_by_name('contacts').is_enabled() == True

@then('the title on my edit page is set to \'test title - edited\'')
def check_updated_title(context):
    assert context.browser.find_element_by_name('title').text.contains('test title - edited')

@then('the title on my edit page is set to \'test description - edited\'')
def check_updated_description(context):
    assert context.browser.find_element_by_name('description').text.contains('test description - edited')

@then('the only tag on my edit page is set to \'test tag - edited\'')
def check_updated_tags(context):
    assert False
    ''' Update this when decided on implementation '''

@then('the contacts on my edit page should be my user and the \'test contact - edited\' user')
def check_updated_contacts(context):
    assert False
    ''' Update this when decided on implementation '''

@given('I am happy with the information on the page')
def update_page_info(context):
    update_title(context)
    update_description(context)
    update_tags(context)
    update_contacts(context)

@then('I am directed to the published page')
def check_user_on_published_page(context):
    assert False
    '''
    # Figure out how to implement #
    '''

@then('the published page is updated with the information I have entered')
def check_publish_page_info(context):
    check_updated_title(context)
    check_updated_description(context)
    check_updated_tags(context)
    check_updated_contacts(context)