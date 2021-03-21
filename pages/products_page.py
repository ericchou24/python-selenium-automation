from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page



class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    CART = (By.ID, 'nav-cart-count')
    SIZE_TOOLTIP = (By.ID, 'a-popover-content-1')
    SIZE_SELECTION_BTN = (By.ID, 'dropdown_selected_size_name')
    SIZE_OPTION_0 = (By.ID, 'size_name_0')
    PRICE_BUY_BOX = (By.ID, 'priceInsiderBuyBox_feature_div')
    COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
    SELECTOR_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')
    NEW_ARRIVALS_BTN = (By.XPATH, '//span[contains(text(), "New Arrivals")]')
    ARRIVALS_DROPDOWN = (By.XPATH, '//div[@class="mega-menu"]')
    SELECTED_DEPARTMENT_CATEGORY = (By.CSS_SELECTOR, "#nav-subnav[data-category='{DEPARTMENT_SUBSTRING}']")

    def _get_locator(self, department):
        return [self.SELECTED_DEPARTMENT_CATEGORY[0], self.SELECTED_DEPARTMENT_CATEGORY[1].replace('{DEPARTMENT_SUBSTRING}', department)]

    def specific_product_page(self, item):
        self.open_url('https://www.amazon.com/gp/product/' + item + '/')

    def hover_over(self):
        new_arrivals = self.driver.find_element(*self.NEW_ARRIVALS_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()
        sleep(1)

    def verify_dropdowns_menu(self):
        dropdown = self.driver.find_elements(*self.ARRIVALS_DROPDOWN)
        assert len(dropdown) == 5, f'Expected 5 but got {len(dropdown)} instead'

    def verify_department(self, department):
        locator = self._get_locator(department)
        self.wait_for_element_appear(*locator)
