from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
tc = unittest.TestCase('__init__')
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")
print("Application title is ",driver.title)
driver.find_element_by_id('search_query_top').send_keys('Hola Mundo')

driver.find_element_by_name('submit_search').click()

time.sleep(3)
result_labels = driver.find_element_by_xpath('//*[@id="center_column"]/p')
tc.assertEqual('No results were found for your search "Hola Mundo"',result_labels.text)
#tc.assertEqual('No results were found for your search "Hola Mundo"',driver.find_element_by_xpath('//*[@id="center_column"]/p'))
time.sleep(5)
driver.find_element_by_link_text('Women').click()

time.sleep(5)

driver.find_element_by_partial_link_text('Dres').click()

time.sleep(4)

#Link text
driver.find_element_by_link_text('Casual Dresses').click

#Partial link text
#driver.find_element_by_partial_link_text('Casual').click()

#classname
#driver.find_element_by_class_name('subcategory-name').click()

#CSS selector
#driver.find_element_by_css_selector('a.subcategory-name').click()

#Xpath
#driver.find_element_by_xpath('//*[@id="subcategories"]/ul/li[1]/h5/a').click()

#Tag name
#driver.find_element_by_tag_name('a').click()

driver.close
driver.quit
