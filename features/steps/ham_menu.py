from behave import when, then
from selenium.webdriver.common.by import By
from time import sleep

HAM_MENU = (By.ID, 'nav-hamburger-menu')

@then('Verify hamburger menu icon is visible')
def verify_ham_menu_present(context):
    context.driver.find_element(*HAM_MENU)