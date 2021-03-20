from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()
    #context.driver.get('https://www.amazon.com/')

@when('Input Watches into Amazon search field')
def input_search(context):
    ##search = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    ##search.send_keys('Watches')
    context.app.main_page.input_amazon_search()

@when('Click on Amazon search icon')
def input_search(context):
    ##push_search = context.driver.find_element(*SEARCH_FIELD)
    ##push_search.click()
    context.app.main_page.click_search_amazon()


@then('Product results for Watches are shown on Amazon')
def verify_found_results_text(context):
    returned_text = context.driver.find_element(*RESULT).text
    print("This is results: " + returned_text)
    expected_text = '"Watches"'

    assert expected_text == returned_text, f'Expected {expected_text}, but got {returned_text} instead'
