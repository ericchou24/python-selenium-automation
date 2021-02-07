from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@given('Open Amazon Product search page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Input Legos into search page and enter')
def input_search(context):
    search = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    search.send_keys('Legos', Keys.ENTER)

@when('Add first result into cart')
def click_first_result(context):
    click_first_result = context.driver.find_element(By.XPATH, '//div[@data-index="2"]')
    click_first_result.click()
    add_first_to_cart = context.driver.find_element(By.ID, 'add-to-cart-button')
    add_first_to_cart.click()

@then('Verify item is in cart')
def verify_in_cart(context):
    add_to_cart_confirmation = context.driver.find_element(By.XPATH, "//div[@id='huc-v2-order-row-confirm-text']//h1").text
    expected_result = 'Added to Cart'
    assert add_to_cart_confirmation == expected_result, f'Expected {expected_result} but got {add_to_cart_confirmation} isntead'
