from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(4)

driver.get('https://www.amazon.com/gp/help/customer/display.html')

search = driver.find_element(By.ID, 'helpsearch')
search.send_keys('Cancel order')
search.send_keys(Keys.ENTER)
##search.submit()

returned_results = driver.find_element(By.XPATH, "//h1[contains(text(),'Cancel Items or Orders')]").text
##print(returned_results)
assert returned_results == "Cancel Items or Orders"
