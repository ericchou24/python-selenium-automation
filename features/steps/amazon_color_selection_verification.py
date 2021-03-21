from behave import when, then
from selenium.webdriver.common.by import By

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')
ALL_COLORS = (By.CSS_SELECTOR, '#variation_color_name img[alt]')
COLOR_SELECTION = (By.XPATH, "//div[@id='variation_color_name']//li//img")


@given('Open Amazon ProductID {item} page')
def open_item_page(context, item):
    context.driver.get('https://www.amazon.com/gp/product/' + item + '/')


@then('Verify user can click through color selection')
def verify_color_selection(context):
    colors = context.driver.find_elements(*COLOR_SELECTION)
    for color_object in colors:
        color = color_object.get_attribute('alt')
        color_object.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        assert color == selected_color, f'Expected {color} but got {selected_color} instead'


