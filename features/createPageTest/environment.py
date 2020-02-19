from selenium import webdriver
from django.core import management

def before_all(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-setuid-sandbox")
    context.browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',chrome_options=chrome_options)
    context.browser.get('https://www.amazon.co.uk')
    print(context.browser.title)
    print(context.browser.current_url)
    print('SUCCESSFULLY INITIATED CHROME')

'''
def before_scenario(context, scenario):
    # Reset the database before each scenario
    # This means we can create, delete and edit objects within an
    # individual scenerio without these changes affecting our
    # other scenarios
    management.call_command('flush', verbosity=0, interactive=False)
'''

def after_all(context):
	context.browser.quit()