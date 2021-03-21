from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.products_page import ProductPage

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')
ALL_COLORS = (By.CSS_SELECTOR, '#variation_color_name img[alt]')
COLOR_SELECTION = (By.XPATH, "//div[@id='variation_color_name']//li//img")

@given('Open Amazon ProductID {item} page')
def open_item_page(context, item):
    context.app.products_page.specific_product_page(item)

@when('{alias} category is selected')
def dropdown_select(context, alias):
    context.app.main_page.select_department(alias)

@when('{item} is searched')
def search_item(context, item):
    context.app.main_page.input_amazon_search(item)
    context.app.main_page.click_search_amazon()

@then('Verify {department} department is selected')
def verify_department(context, department):
    context.app.products_page.verify_department(department)

@then('Verify user can click through color selection')
def verify_color_selection(context):
    colors = context.driver.find_elements(*COLOR_SELECTION)
    for color_object in colors:
        color = color_object.get_attribute('alt')
        color_object.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        assert color == selected_color, f'Expected {color} but got {selected_color} instead'



@then('Hovers over New Arrivals')
def hover_new_arrival(context):
    context.app.products_page.hover_over()


@then('Verifies user sees the deals')
def verify_deals(context):
    context.app.products_page.verify_dropdowns_menu()

