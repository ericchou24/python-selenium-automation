from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(4)

driver.get('https://www.amazon.com/')


##driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Watches')

search = driver.find_element(By.ID, 'twotabsearchtextbox')
search.send_keys('5950x')

##push_search = driver.find_element(By.ID, 'nav-search-submit-button').click()

push_search = driver.find_element(By.ID, 'nav-search-submit-button')
push_search.click()

returned_text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
expected_text = '"5950x"'

assert expected_text == returned_text, f'Expected {expected_text}, but got {returned_text} instead'
##assert expected_text == returned_text, 'Expected {}, but got {} instead'.format(expected_text, returned_text)

##driver.quit()

"""
AMD Shop example, where to pick this up from
https://www.amazon.com/AMD-Ryzen-5900X-24-Thread-Processor/dp/B08164VTWH/ref=sr_1_4?dchild=1&keywords=5950x&qid=1612166139&sr=8-4
"""
