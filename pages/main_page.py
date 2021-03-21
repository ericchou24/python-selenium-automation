from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select

class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    CATEGORY_SELECTION = (By.CSS_SELECTOR, 'select.nav-search-dropdown')

    ##def click_category(self):
    ##    self.click(*self.CATEGORY_SELECTION)
    ##    sleep(5)

    def select_department(self, alias):
        select = Select(self.driver.find_element(*self.CATEGORY_SELECTION))
        select.select_by_value(f'search-alias={alias}')


    def open_main_page(self):
        self.open_url('https://www.amazon.com/')

    def input_amazon_search(self, search_query):
        self.input_text(search_query, *self.SEARCH_FIELD)

    def click_search_amazon(self):
        self.click(*self.SEARCH_ICON)
