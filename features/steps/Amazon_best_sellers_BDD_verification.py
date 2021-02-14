from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

webpage = 'https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers'
nav_bar = 'zg_tabs'
best_seller_links = (By.XPATH, "//div[@id='zg_tabs']/ul/li")


@given('Open Amazon Best Sellers Page')
def open_amazon(context):
    context.driver.get(webpage)

@then('Verify there are five links')
def verify_in_cart(context):
    search = context.driver.find_elements(*best_seller_links)
    assert len(search) == 5, f'Expected 5 links, but got {len(search)}'

