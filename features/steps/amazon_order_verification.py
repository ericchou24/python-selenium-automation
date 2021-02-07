from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon home page')
def open_google(context):
    context.driver.get('https://www.amazon.com/')

@when('Orders is clicked on navigation')
def input_search(context):
    search = context.driver.find_element(By.ID, 'nav-orders')
    search.click()


@then('Verify Sign in page Opened')
def verify_found_results_text(context):
    ##returned_text = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Sign-In')]").text
    returned_text = context.driver.find_element(By.XPATH, "//div[@class='a-box-inner a-padding-extra-large']//h1").text
    print("This is results: " + returned_text)
    expected_text = 'Sign-In'
## Notes: text is not the most stable method like used in the commented out line of code
## Use / to select a node's immediate children.
## Use // to select a node, its children, its grandchildren, and so on recursively.
    assert expected_text == returned_text, f'Expected {expected_text}, but got {returned_text} instead'
