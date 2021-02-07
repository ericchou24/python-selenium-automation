from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@given('Open Amazon help center page')
def open_google(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when('Cancel Orders inputted into Help Center input page')
def input_search(context):
    search = context.driver.find_element(By.ID, 'helpsearch')
    search.send_keys('Cancel order', Keys.ENTER)

@then('Verify correct Cancel Items or Orders page')
def verify_search_results_text(context):
    returned_results = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Cancel Items or Orders')]").text
    expected_text = "Cancel Items or Orders"
    assert returned_results == returned_results, f'Expected {expected_text}, but got {returned_results} instead'