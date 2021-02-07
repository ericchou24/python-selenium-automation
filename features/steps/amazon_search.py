from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_google(context):
    context.driver.get('https://www.amazon.com/')

@when('Input Watches into Amazon search field')
def input_search(context):
    search = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    search.send_keys('Watches')


@when('Click on Amazon search icon')
def input_search(context):
    push_search = context.driver.find_element(By.ID, 'nav-search-submit-button')
    push_search.click()



@then('Product results for Watches are shown on Amazon')
def verify_found_results_text(context):
    returned_text = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    print("This is results: " + returned_text)
    expected_text = '"Watches"'

    assert expected_text == returned_text, f'Expected {expected_text}, but got {returned_text} instead'
