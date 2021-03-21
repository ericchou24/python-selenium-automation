from pages.main_page import MainPage
from pages.amazon_orders_cart_check import Orders_Cart_Page
from pages.products_page import ProductPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.amazon_orders_cart_check = Orders_Cart_Page(self.driver)
        self.products_page = ProductPage(self.driver)
        # self.result_page = MainPage(self.driver)
