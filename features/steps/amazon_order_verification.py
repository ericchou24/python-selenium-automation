from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon home page')
def open_google(context):
    ##context.driver.get('https://www.amazon.com/')
    context.app.amazon_orders_cart_check.open_main_page()

@when('Click Amazon Orders link')
def input_search(context):
    ##search = context.driver.find_element(By.ID, 'nav-orders')
    ##search.click()
    context.app.amazon_orders_cart_check.click_orders()


@then('Verify {query} is opened')
def verify_sign_in_opened(context, query):
    ##returned_text = context.driver.find_element(By.XPATH, "//div[@class='a-box-inner a-padding-extra-large']//h1").text
    ##print("This is results: " + returned_text)
    ##expected_text = 'Sign-In'
    ##assert expected_text == returned_text, f'Expected {expected_text}, but got {returned_text} instead'
    context.app.amazon_orders_cart_check.verify_order_signin(query)
