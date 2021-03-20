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

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text} instead'

