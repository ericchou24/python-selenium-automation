class Page:

    def __init__(self, driver):
        self.driver = driver

    def click (self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locators):
        e = self.driver.find_element(*locators)
        e.clear()
        e.send_keys(text)

    def open_url(self, url):
        self.driver.get(url)

