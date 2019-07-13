'''
@author: wojtekhaj
'''

from selenium import webdriver
from selenium.webdriver import ActionChains

path = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

driver=webdriver.Chrome(path)
driver.get("https://www.amazon.co.uk")
main_page_title="Amazon.co.uk: Low Prices in Electronics, Books, Sports Equipment & more"
assert main_page_title in driver.title
driver.maximize_window()
driver.implicitly_wait(10)

#go to department - sports fitnes
department_xpath="//span[@class='nav-line-2' and contains (text(), 'Department')]"
fitness_xpath="//div[@class='popover-grouping']//h2[contains (text(), 'Sports & Outdoors')]//..//a[contains(text(), 'Fitness')]"
see_more_xpath="//div[@id='leftNav']//h4[contains(text(), 'Featured Brands')]//..//span[@class='a-size-small' and contains (text(), 'See more')]"
a_letter_xpath="//div[@id='indexBarHeader']//a[contains (text(), 'A')]"
adidas_xpath="//div[@id='refinementList']//span[contains (text(), 'adidas')]"
first_header="Amazon.co.uk - Earth's Biggest Selection"
second_header="Fitness: Sports & Outdoors: Clothing, Yoga, Accessories, Strength Training Equipment, Pilates & More: Amazon.co.uk"
third_header="Amazon.co.uk: see all results"

driver.find_element_by_xpath(department_xpath).click()
assert first_header in driver.title
driver.find_element_by_xpath(fitness_xpath).click()
assert second_header in driver.title
driver.find_element_by_xpath(see_more_xpath).click()
assert third_header in driver.title
driver.find_element_by_xpath(a_letter_xpath).click()
element=driver.find_element_by_xpath(adidas_xpath)
ActionChains(driver).move_to_element(element).perform()
driver.save_screenshot("adidas.png")
driver.close()





