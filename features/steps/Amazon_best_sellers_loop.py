from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

## Since we already previously had a best sellers function that asserted and stored the variables,
# do we need to re-instantiate the variables like below?  The system found the right commands

webpage = 'https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers'
nav_bar = 'zg_tabs'
best_seller_links = (By.XPATH, "//div[@id='zg_tabs']/ul/li")

##only new one being used for this
best_seller_headers = (By.CSS_SELECTOR, "#zg_banner_text_wrapper")

@then('Click through each link and verify that new page opens')
def link_click_through(context):
    for item in range(len(context.search)):
        element = context.driver.find_elements(*best_seller_links)
        nav_name = element[item].text
        element[item].click()
        page_headers = context.driver.find_element(*best_seller_headers).text
        assert nav_name in page_headers, f'Expected to see {nav_name}, but got {page_headers} page instead'


