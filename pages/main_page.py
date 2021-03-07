from selenium.webdriver.common.by import By
from TempTest.pages import Page

class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')

    def open_main_page(self):
        self.open_url('https://www.amazon.com/')

    def input_amazon_search(self):
        self.input_text('Watches', *self.SEARCH_FIELD)

    def click_search_amazon(self):
        self.click(*self.SEARCH_ICON)
