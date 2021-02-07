from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@given('Opens Amazon Home Page')
def open_chrome(context):
    context.driver.get('https://www.amazon.com/')

@when('Cart is clicked on Navigation')
def open_shopping_cart(context):
    search = context.driver.find_element(By.ID, 'nav-cart-count-container')
    search.click()

@then('Verify Cart is empty')
def verify_empty_cart(context):
    returned_text = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']//h2").text
    expected_text = 'Your Amazon Cart is empty'
    assert returned_text == expected_text, f'Expected {expected_text}, but got {returned_text} instead'
