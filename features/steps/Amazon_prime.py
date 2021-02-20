from behave import when, then, given
from selenium.webdriver.common.by import By

BENEFIT_BOXES = (By.CSS_SELECTOR, '.benefit-box')

@given('Open Amazon Prime Page')
def open_prime(context):
    context.driver.get('https://amazon.com/amazonprime')

@then('Verify {expected_boxes} benefit boxes are displayed')
def verify_boxes(context, expected_boxes):
    expected_boxes = int(expected_boxes)
    actual_boxes = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(actual_boxes) == expected_boxes, f'Expected {expected_boxes} but we see {len(actual_boxes)}'
"""    
    OR make the comparison variable an INT. Comparing INT to an INT instead of STR to an INT
    assert len(actual_boxes) == int(expected_boxes), f'Expected {expected_boxes} but we see {len(actual_boxes)}'
"""