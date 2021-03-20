from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@given('Opens Amazon Home Page')
def open_chrome(context):
    context.app.amazon_orders_cart_check.open_main_page()

@when('Click on cart icon')
def open_shopping_cart(context):

    context.app.amazon_orders_cart_check.click_cart()

@then("Verify {query} text present")
def verify_empty_cart(context, query):
    context.app.amazon_orders_cart_check.verify_cart_results(query)
