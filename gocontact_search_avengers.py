'''
@author: wojtekhaj
'''

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import re

path = '/home/wojtekhaj/mindera/qa-sortable-challenge/solution/chromedriver'

driver=webdriver.Chrome(path)
driver.get("https://www.amazon.co.uk")
main_page_title="Amazon.co.uk: Low Prices in Electronics, Books, Sports Equipment & more"
assert main_page_title in driver.title
driver.maximize_window()
driver.implicitly_wait(10)


#check for avengers
search_film_phraze="avengers"
main_search_field_xpath= "//input[@id='twotabsearchtextbox']"

search_object=driver.find_element_by_xpath(main_search_field_xpath)
search_object.send_keys(search_film_phraze)
search_object.send_keys(Keys.ENTER)

#check for avenger assemble
search_title="Amazon.co.uk: avengers"
assert search_title in driver.title
film_title="Avengers Assemble"
film_title_xpath="//span[contains(text(),'Avengers Assemble')]"
                                                         
#src = driver.page_source
#film_found = re.search(film_title, src)
#driver.assertNotEqual(film_found, None)

element=driver.find_element_by_xpath(film_title_xpath)
ActionChains(driver).move_to_element(element).perform()
driver.save_screenshot("Avengers_assemble.png")

#check if has shield in the description
film_xpath="//span[@class='a-size-medium a-color-base a-text-normal' and contains (text(),'Assemble')]"
shield_xpath="//p[contains (text(),'S.H.I.E.L.D')]"

driver.find_element_by_xpath(film_xpath).click()

driver.find_element_by_xpath(shield_xpath).click()

driver.save_screenshot("shield.png")
#See videos and save 10 s video
film_page_title="Amazon.co.uk: Watch Avengers Assemble | Prime Video"
assert film_page_title in driver.title
trailer_xpath="//a[@data-video-type='Trailer']"

driver.find_element_by_xpath(trailer_xpath).click()

driver.save_screenshot("trailer.png")
driver.close()





