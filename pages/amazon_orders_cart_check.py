from selenium.webdriver.common.by import By

from pages.base_page import Page

class Orders_Cart_Page(Page):
    NAV_CART = (By.ID, 'nav-cart-count-container')
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "div[class='a-row sc-your-amazon-cart-is-empty']")
    EXPECTED_TEXT = 'Your Amazon Cart is empty'
    ORDERS_BTN = (By.ID, 'nav-orders')
    SIGN_IN_TEXT = (By.XPATH, "//div[@class='a-box-inner a-padding-extra-large']//h1")

    def open_main_page(self):
        self.open_url('https://www.amazon.com/')

    def click_cart(self):
        self.click(*self.NAV_CART)

    def click_orders(self):
        self.click(*self.ORDERS_BTN)

    def verify_cart_results(self, query):
        self.verify_text(query, *self.EMPTY_CART_TEXT)

    def verify_order_signin(self, result_word):
        self.verify_text(result_word, *self.SIGN_IN_TEXT.text)