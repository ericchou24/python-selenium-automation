from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

TERMS_CONDITIONS = (By.CSS_SELECTOR, "a[href*='https://www.amazon.com/gp/feature.html?docId=1000625601']")
APP_IMG = (By.CSS_SELECTOR, "#mgt-email-sms-download-header")

@given('Open Amazon T&C page')
def open_amazon_tc(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle

@when('Click on Amazon applications link (*see image below)')
def click_amazon_link(context):
    context.driver.find_element(*TERMS_CONDITIONS).click()

@when('Switch to the newly opened window')
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.driver.switch_to.window(context.driver.window_handles[1])

@then('Amazon app page is opened')
def new_amazon_app_page(context):
    page = context.driver.find_element(*APP_IMG).text
    expected = 'Download the app today!'
    assert page == expected, f'We see: {page}, instead of {expected}'

@then('User can close new window and switch back to original')
def back_to_original_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)